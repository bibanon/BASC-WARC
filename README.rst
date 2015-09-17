BASC-Warc
=========

`Bibliotheca Anonoma's <http://bibanon.org/>`_ library for creating and managing WARC files.

This library is in the planning / pre-alpha stage. It is still being written, and is not yet suitable for any real-world usage at this point. While we are still writing and designing the API, anything can change without any notice.

Pull requests are appreciated, but due to the early stage of development you may need to overhaul your PR as we update the project code.

This library is primarily written for `BASC-Archiver <https://github.com/bibanon/BASC-Archiver>`_, to be used by a (new?) downloading library.


Planned Features
----------------

* Python 2/3 compatibility.
* Thread-safe.
* Ability to gz arbitrary adjacent members together if the spec allows it (for instance, gzip the `response` and `resource` members of one request together, to take advantage of the duplicated information).
* Streaming reading/writing of WARC files, for dealing with very large files on systems with smaller amounts of memory.
* CDX file creation and management.
* Included scripts that do useful work, possibly allowing viewing or extracting information and files from WARCs / appending WARCs / creating CDX files from WARCs, similar to `megawarc <https://github.com/alard/megawarc>`_ or `CDX-Writer <https://github.com/rajbot/CDX-Writer>`_.


License
-------

Written in 2015 by Daniel Oaks <daniel@danieloaks.net>

To the extent possible under law, the author(s) have dedicated all copyright and related and neighboring rights to this software to the public domain worldwide. This software is distributed without any warranty.

You should have received a copy of the CC0 Public Domain Dedication along with this software. If not, see `http://creativecommons.org/publicdomain/zero/1.0/ <http://creativecommons.org/publicdomain/zero/1.0/>`_.
