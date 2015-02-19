#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#==============================================================================
# Written by Rentouch 2013 - http://www.rentouch.ch
#==============================================================================

from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]

# -----------------------------------------------------------------------------
exec(open('cefbrowser/version.py').read())  # Will store __version__

# setup
setup(name='cefbrowser',
      version=__version__,
      author='Rentouch GmbH',
      author_email='info@rentouch.ch',
      url='http://www.rentouch.ch',

      package_data={'cefbrowser': ['images/*.png', '*.kv']},

      packages=['cefbrowser', ],

      install_requires=reqs
)

# -----------------------------------------------------------------------------

