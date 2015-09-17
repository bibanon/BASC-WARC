WARC Record blocks
==================

You use any of these classes as a content block for a :class:`basc_warc.Record` object.


Bytes
-----

This is the standard type of block, and lets you expose a series of bytes (a file, HTTP request, etc) as a block for a :class:`basc_warc.Record`.

.. autoclass:: basc_warc.RecordBlock


``warcinfo`` Block
------------------

This type of block is used for ``warcinfo`` Records, and lets you easily set keys and values.

.. autoclass:: basc_warc.WarcinfoBlock

.. automethod:: basc_warc.WarcinfoBlock.set_field
