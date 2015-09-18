BASC-WARC
=========

`Bibliotheca Anonoma's <http://bibanon.org/>`_ library for creating and managing WARC files.

This library is in the planning / pre-alpha stage. It is still being written, and is not yet suitable for any real-world usage at this point. While we are still writing and designing the API, anything can change without any notice.

Pull requests are appreciated, but due to the early stage of development you may need to overhaul your PR as we update the project code.

This library is primarily being written for `BASC-Archiver <https://github.com/bibanon/BASC-Archiver>`_, and planned to be integrated into a new/existing downloading library.

`Hosted Documentation <http://basc-warc.readthedocs.org/en/latest/>`_

Planned Features
----------------

* Python 2/3 compatibility.
* Thread-safe.
* Streaming reading/writing of WARC files, for dealing with very large files on systems with smaller amounts of memory.
* CDX file creation and management.
* Included scripts that do useful work, possibly allowing viewing or extracting information and files from WARCs / appending WARCs / creating CDX files from WARCs, similar to `megawarc <https://github.com/alard/megawarc>`_, `CDX-Writer <https://github.com/rajbot/CDX-Writer>`_, or `warctools <https://github.com/internetarchive/warctools>`_.


Dependencies
------------

This module uses the `pyiso8601 <https://bitbucket.org/micktwomey/pyiso8601>`_ package.


License
-------

Written in 2015 by Daniel Oaks <daniel@danieloaks.net>

To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.

You should have received a copy of the CC0 Public Domain Dedication along with this software. If not, see `http://creativecommons.org/publicdomain/zero/1.0/ <http://creativecommons.org/publicdomain/zero/1.0/>`_.
