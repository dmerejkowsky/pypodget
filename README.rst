PyPodget
========


This is a *very* basic rewrite of `podget <http://podget.sourceforge.net/>`_
in Python.


Usage
-----

You must edit the ``~/.condfig/pypodget/pypodget.conf``
file before using this software

First, add a ``core`` section to choose an output
directory ::

  [core]
  output = ~/podcasts

Then, add your podcasts this way ::

  [Name]
  url = http://example.com/feed.xml

Then run ::

  pypodget

That's it, podcasts will be downloaded to
``<output dir>/<podcast name>/<date.mp3>``


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
