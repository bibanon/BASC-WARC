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
import collections
import uuid

import iso8601


# identifiers
def uuid_urn():
    """Return a UUID suitable for use in WARC files."""
    return '<urn:uuid:{}>'.format(str(uuid.uuid4()))


# content digest
def content_digest(content):
    raise NotImplementedError


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


# CaseInsensitiveDict from requests.
#
# Copyright 2015 Kenneth Reitz
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
class CaseInsensitiveDict(collections.MutableMapping):
    """
    A case-insensitive ``dict``-like object.
    Implements all methods and operations of
    ``collections.MutableMapping`` as well as dict's ``copy``. Also
    provides ``lower_items``.
    All keys are expected to be strings. The structure remembers the
    case of the last key to be set, and ``iter(instance)``,
    ``keys()``, ``items()``, ``iterkeys()``, and ``iteritems()``
    will contain case-sensitive keys. However, querying and contains
    testing is case insensitive::
        cid = CaseInsensitiveDict()
        cid['Accept'] = 'application/json'
        cid['aCCEPT'] == 'application/json'  # True
        list(cid) == ['Accept']  # True
    For example, ``headers['content-encoding']`` will return the
    value of a ``'Content-Encoding'`` response header, regardless
    of how the header name was originally stored.
    If the constructor, ``.update``, or equality comparison
    operations are given keys that have equal ``.casefold()``s, the
    behavior is undefined.
    """

    def __init__(self, data=None, **kwargs):
        self._store = dict()
        if data is None:
            data = {}
        self.update(data, **kwargs)

    def __setitem__(self, key, value):
        # Use the lowercased key for lookups, but store the actual
        # key alongside the value.
        self._store[key.casefold()] = (key, value)

    def __getitem__(self, key):
        return self._store[key.casefold()][1]

    def __delitem__(self, key):
        del self._store[key.casefold()]

    def __iter__(self):
        return (casedkey for casedkey, mappedvalue in self._store.values())

    def __len__(self):
        return len(self._store)

    def lower_items(self):
        """Like iteritems(), but with all lowercase keys."""
        return (
            (lowerkey, keyval[1])
            for (lowerkey, keyval)
            in self._store.items()
        )

    def __eq__(self, other):
        if isinstance(other, collections.Mapping):
            other = CaseInsensitiveDict(other)
        else:
            return NotImplemented
        # Compare insensitively
        return dict(self.lower_items()) == dict(other.lower_items())

    # Copy is required
    def copy(self):
        return CaseInsensitiveDict(self._store.values())

    def __repr__(self):
        return str(dict(self.items()))
