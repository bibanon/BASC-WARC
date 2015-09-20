:class:`basc_warc.RecordHeader` - WARC Record Header
====================================================

This class is a header for a :class:`basc_warc.Record` object.


Fields
------

The following methods let you set standard WARC fields.

.. autoclass:: basc_warc.RecordHeader

.. automethod:: basc_warc.RecordHeader.set_field


Simple field access
-------------------

These are convenient ways to access certain fields.

.. autoattribute:: basc_warc.RecordHeader.record_id

.. autoattribute:: basc_warc.RecordHeader.date
