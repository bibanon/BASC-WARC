# -*- coding: utf-8 -*-
# BASC-Warc
"""Create and manage WARC files."""
import sys
import threading

__version__ = '0.0.1'

WARC_VERSION = b'WARC/1.0'
WARC_SOFTWARE = (b'BASC-Warc/' + __version__.encode() +
                 b' Python/' + sys.version.encode())
CRLF = b'\r\n'


class WarcFile(object):
    """A WARC (Web ARChive) file."""

    def __init__(self, records=[]):
        self.records = records
        self.records_lock = threading.Lock()

    # output
    def bytes(self, compress_records=False):
        """Return bytes to write.

        Args:
            compress_records (bool): Whether to apply gzip compression to records.

        Returns:
            Bytes that represent this WARC file.
        """
        warc = bytes()

        with self.records_lock:
            for record in self.records:
                if compress_records:
                    print('Cannot compress records yet.')
                else:
                    warc += record.bytes()

        return warc

    # adding records
    def add_record(self, record):
        """Add the given WarcRecord to our records.

        Args:
            record: Record to add to this WARC file.

        Returns:
            The index of the added record.
        """
        record_indexes = self.add_records(record)
        return record_indexes[0]

    def add_records(self, *records):
        """Add the given WarcRecord objects to our records.

        Args:
            record (list of WarcRecord): Records to add to this WARC file.

        Returns:
            Indexes of the added records.
        """
        record_indexes = []

        with self.records_lock:
            for record in records:
                record_index = len(self.records)
                record_indexes.append(record_index)

                self.records.append(record)

        return record_indexes

    def add_new_record(self, record_type, block=None, fields={}):
        """Add an arbitrary new record.

        Args:
            record_type (string): WARC record type.
            block (bytes): Content block for this record.
            fields (dict): Fields for this record.

        Returns:
            Index of the new added record.
        """
        new_record = WarcRecord(record_type, block=block, fields=fields)
        record_index = self.add_record(new_record)
        return record_index

    def add_warcinfo_record(self, fields={}, operator=None, software=None,
                            robots=None, hostname=None, ip=None,
                            http_header_user_agent=None, http_header_from=None,
                            **kwargs):
        """Add a warcinfo record to this file.

        Args:
            fields (dict): Fields for this record.
            operator (string): Contact information for the operator who created this resource.
                A name or a name and email address is recommended.
            software (string): Software and software version used to create this WARC resource
                (defaults to BASC-Warc's version informaton).
            robots (string): The robots policy followed by the harvester creating this WARC
                resource. The string ``'classic'`` indicates the 1994 web robots exclusion
                standard rules are being obeyed.
            hostname (string): The hostname of the machine that created this WARC resource,
                such as "crawling17.archive.org".
            ip (string): The IP address of the machine that created this WARC resource, such as
                "123.2.3.4".
            http_header_user_agent (string): The HTTP 'user-agent' header usually sent by the
                harvester along with each request. If 'request' records are used to save
                verbatim requests, this information is redundant.
            http_header_from (string): The HTTP 'From' header usually sent by the harvester
                along with each request (redundant when 'request' records are used, as above).

        Returns:
            Index of the new added record.
        """
        if operator:
            fields['operator'] = operator
        if software:
            fields['software'] = software
        if robots:
            fields['robots'] = robots
        if hostname:
            fields['hostname'] = hostname
        if ip:
            fields['ip'] = ip
        if http_header_user_agent:
            fields['http-header-user-agent'] = http_header_user_agent
        if http_header_from:
            fields['http-header-from'] = http_header_from

        for key, value in kwargs:
            fields[key] = value

        record_index = self.add_new_record('warcinfo', fields=fields)
        return record_index


class WarcRecord(object):
    """A record in a WARC file."""

    def __init__(self, record_type, header=None, block=None):
        self.record_type = record_type
        self.header = header
        self.block = block

    def bytes(self):
        """Return bytes to write."""
        self.header.set_field('Content-Length', self.block.length())
        return self.header.bytes() + CRLF + self.block.bytes() + CRLF + CRLF


class WarcRecordHeader(object):
    """A header for a WARC record."""

    def __init__(self, fields={}):
        self.fields = fields

    def set_field(self, name, value):
        """Set field to the given value."""
        self.field[name] = value

    def bytes(self):
        """Return bytes to write."""
        field_bytes = bytes()

        for key, value in self.fields.items():
            if isinstance(key, str):
                key = key.encode()
            if isinstance(value, str):
                value = value.encode()

            field_bytes += key + b': ' + value

        return WARC_VERSION + CRLF + field_bytes + CRLF


class WarcinfoBlock(object):
    """Block for a warcinfo record."""

    def __init__(self, fields={}):
        self.fields = fields
        self._cache = None

    def set_field(self, name, value):
        """Set field to given value."""
        self.fields[name] = value
        self._cache = None

    def bytes(self):
        """Return bytes to write."""
        if self._cache is None:
            # assemble block items
            info_fields = []

            for key, value in self.fields.items():
                if isinstance(key, str):
                    key = key.encode()
                if isinstance(value, str):
                    value = value.encode()

                info_fields.append(key + b': ' + value)

            # assemble into final block
            info = CRLF.join(info_fields)

            self._cache = info

        return self._cache

    def length(self):
        """Return length in bytes."""
        return len(self.bytes())
