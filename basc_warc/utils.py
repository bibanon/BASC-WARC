# -*- coding: utf-8 -*-
# BASC-WARC utility functions
#
# Written in 2015 by Daniel Oaks <daniel@danieloaks.net>
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
"""Utility functions used by basc_warc."""
from datetime import datetime

import iso8601


# key sorting
def sort_manual_keys(*sorted_keys):
    """Create a key function that sorts the given keys first."""
    _key_order = []
    for key in sorted_keys:
        if hasattr(key, 'lower'):
            key = key.lower()
        _key_order.append(key)

    def key_fn(key):
        if hasattr(key, 'lower'):
            key = key.lower()

        for i, sorted_key in enumerate(_key_order):
            if key == sorted_key:
                return '{}_{}'.format(i, key)

        return '{}_{}'.format(len(_key_order), key)

    return key_fn


# timestamps
def ts_to_datetime(timestamp):
    """Convert a WARC timestamp (ISO8601 subset) to a DateTime object."""
    return iso8601.parse_date(timestamp)


def datetime_to_ts(date_time):
    """Convert a DateTime object into a WARC 1.0 timestamp."""
    return date_time.strftime('%Y-%m-%dT%H:%M:%SZ')


# field names / values
def writable_field_name(name):
    """Given a field name, return a writable series of bytes."""
    if isinstance(name, str):
        out = bytes(name.encode('utf8'))
    elif isinstance(name, bytes):
        out = name

    return out


def writable_field_value(value):
    """Given a field value, return a writable series of bytes."""
    if isinstance(value, str):
        out = bytes(value.encode('utf8'))
    elif isinstance(value, int):
        out = bytes(str(value).encode('utf8'))
    elif isinstance(value, datetime):
        out = bytes(datetime_to_ts(value).encode('utf8'))
    elif isinstance(value, bytes):
        out = value

    return out
