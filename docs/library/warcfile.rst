:class:`basc_warc.WarcFile` --- Managing WARC files
===================================================

This class is how you create and manage WARC files.

.. autoclass:: basc_warc.WarcFile


Adding specific records
-----------------------

These functions let you add standard types of records easily.

.. automethod:: basc_warc.WarcFile.add_warcinfo_record


Adding custom records
---------------------

These functions let you add :class:`basc_warc.Record` objects directly into this WARC file.

In a threaded application, if you are adding multiple records that relate to each other, you should use the :meth:`basc_warc.WarcFile.add_records` function, as this will ensure the given records are adjacent.

.. automethod:: basc_warc.WarcFile.add_record

.. automethod:: basc_warc.WarcFile.add_records


Writing files out
-----------------

To write files out, you simply use the :meth:`basc_warc.WarcFile.bytes` function and write the output to a file.

.. automethod:: basc_warc.WarcFile.bytes
