BASC-Warc
=========

`Bibliotheca Anonoma's <http://bibanon.org/>`_ library for creating and managing WARC files.

.. WARNING::
    This is not even in alpha right now. This is in the planning / pre-alpha stage. If you use this, ANYTHING can change without any notice whatsoever, everything can be overhauled, and development may even stop entirely without any warning.

This library is primarily being written for `BASC-Archiver <https://github.com/bibanon/BASC-Archiver>`_, and planned to be integrated into a new/existing downloading library.


Planned Features
----------------

* Python 2/3 compatibility.
* Thread-safe.
* Ability to gz arbitrary adjacent members together if the spec allows it (for instance, gzip the `response` and `resource` members of one request together, to take advantage of the duplicated information).
* Streaming reading/writing of WARC files, for dealing with very large files on systems with smaller amounts of memory.
* CDX file creation and management.
* Included scripts that do useful work, possibly allowing viewing or extracting information and files from WARCs / appending WARCs / creating CDX files from WARCs, similar to `megawarc <https://github.com/alard/megawarc>`_, `CDX-Writer <https://github.com/rajbot/CDX-Writer>`_, or `warctools <https://github.com/internetarchive/warctools>`_.


License
-------

Written in 2015 by Daniel Oaks <daniel@danieloaks.net>

To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.

You should have received a copy of the CC0 Public Domain Dedication along with this software. If not, see `http://creativecommons.org/publicdomain/zero/1.0/ <http://creativecommons.org/publicdomain/zero/1.0/>`_.


Library
-------

.. toctree::
   :maxdepth: 2
   :numbered:

   library/warcfile


:ref:`genindex`
---------------
