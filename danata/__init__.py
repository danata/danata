"""
Danata
========

    Danata is a Python package for graph-based information transformation framework
    which can help the process of read-transform-write data conviniently.

    https://danata.github.com/

Using
-----

    Just write in Python

    T.B.D.
"""
#    Copyright (C) 2016 by
#    Youngsung Kim <grnydawn@gmail.com>
#    All rights reserved.
#
# Add platform dependent shared library path to sys.path
#

from __future__ import absolute_import

import sys
if sys.version_info[:2] < (2, 7):
    MSG = "Python 2.7 or later is required for Danata (%d.%d detected)."
    raise ImportError(MSG % sys.version_info[:2])
del sys

# Release data
from networkx import release

__author__ = '%s <%s>\n%s <%s>\n%s <%s>' % \
    (release.authors['Youngsung'])
__license__ = release.license

__date__ = release.date
__version__ = release.version

__bibtex__ = """Not published yet."""

# These are import orderwise
from danata.exception import *
import danata.external
import danata.utils

import danata.classes
from danata.classes import *

import danata.readwrite
from danata.readwrite import *

import danata.transform
from danata.transform import *
