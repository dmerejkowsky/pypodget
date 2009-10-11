#!/usr/bin/env python

from distutils.core import setup
import podget
setup(name='pypodget',
      version= pycp.__version__,
      description='Rewrite of podget in python',
      long_description = pycp.__doc__,
      requires=[''],
      author=pycp.__author__,
      author_email=pycp.__author_email__,
      url='http://sd-5791.dedibox.fr/prog/pypodget',
      py_modules=['podget']
      license='BSD',
     )
