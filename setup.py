#!/usr/bin/env python
from distutils.core import setup
import gears


setup(name='gears',
      author='Vanderbilt Computer Society',
      author_email='info@vandycs.org',
      url='http://github.com/vandycs/pygears',
      version=gears.__version__,
      packages=[
          'gears',
      ],
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Microsoft :: Windows :: Windows NT/2000',
          'Programming Language :: Python :: 2.7',
          'Topic :: Games/Entertainment',
          'Topic :: Multimedia :: Graphics',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ]
)
