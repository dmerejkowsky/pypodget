PyPodget
========


This is a *very* basic rewrite of `podget <http://podget.sourceforge.net/>`_
in Python.


Usage
-----

You must edit the ``~/.condfig/pypodget/pypodget.conf``
file before using this software

Add your podcasts this way ::

  [Name]
  url = http://example.com/feed.xml

Then run ::

  pypodget

That's it.


Dependencies
-------------

* ``Python3``
* ``feedparser`` (required)
* ``progressbar`` (optional)

Development
-----------

``PyPodget`` is hosted on github: https://github.com/yannicklm/pypodget


License
-------

This software is distributed under a BSD license.
(see COPYING for details)
