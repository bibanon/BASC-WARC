#!/usr/bin/env python
# -*- coding: utf-8 -*-
# BASC Warc
import sys

__version__ = '0.0.1'

WARC_VERSION = b'WARC/1.0'
WARC_SOFTWARE = (b'BASC-Warc/' + __version__.encode() +
                 b' Python/' + sys.version.encode())


class WarcFile(object):
    """A WARC (Web ARChive) file."""

    def __init__(self, records=[]):
        self.records = records

    def add_record(self, record_type, block=None, fields=[], **kwargs):
        """Add an arbitrary new record."""
        new_record = WarcRecord(record_type, block=block, fields=fields)
        self.records.append(new_record)

    def add_warcinfo_record(self, fields={}, operator=None, software=None,
                            robots=None, hostname=None, ip=None,
                            http_header_user_agent=None, http_header_from=None,
                            **kwargs):
        """Add a warcinfo record to this file."""
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

        self.add_record('warcinfo', fields=fields)


class WarcRecord(object):
    """A record in a WARC file."""

    def __init__(self, record_type, block=None, fields=[]):
        self.version = WARC_VERSION
        self.block = block
        self.fields = fields


class WarcinfoBlock(object):
    """Block for a warcinfo record."""

    def __init__(self, fields={}):
        self.fields = fields

    def _get_bytes(self):
        # assemble block items
        info_fields = []

        for key, value in self.fields.items():
            info_fields.append(key.encode() + b': ' + value.encode())

        # assemble into final block
        info = b'\r\n'.join(info_fields)

        return info
