#!/usr/bin/env python

from distutils.core import setup
setup(name='pypodget',
      version      = "2.0",
      requires     = ["feedparser", "progressbar"],
      description  = "Rewrite of podget in python",
      author       = "Yannick LM",
      author_email = "yannicklm1337@gmail.com",
      url          = 'https://github.com/yannicklm/pypodget',
      scripts      = ['pypodget'],
      license      = 'BSD',
     )
