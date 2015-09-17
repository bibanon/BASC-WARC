:class:`basc_warc.WarcFile` --- Managing WARC files
===================================================

.. class:: basc_warc.WarcFile

This class is how you create and manage WARC files.


Adding specific records
-----------------------

These functions let you add standard types of records easily.

.. automethod:: basc_warc.WarcFile.add_warcinfo_record


Adding custom records
---------------------

These functions let you add :class:`basc_warc.Record` objects directly into this WARC file.

In a threaded application, if you are adding multiple records that relate to each other, you should use the :method:`basc_warc.WarcFile.add_records` function, as this will ensure the given records are adjacent.

.. automethod:: basc_warc.WarcFile.add_record

.. automethod:: basc_warc.WarcFile.add_records
