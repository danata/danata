# -*- coding: utf-8 -*-
"""
**********
Exceptions
**********

Base exceptions and errors for Danata.

"""
__author__ = """Youngsung Kim (grnydawn@gmail.com)"""
#    Copyright (C) 2016 by
#    Youngsung Kim <grnydawn@gmail.com>
#    All rights reserved.
#

# Exception handling

# the root of all Exceptions
class DanataException(Exception):
    """Base class for exceptions in Danata."""

class DanataError(DanataException):
    """Exception for a serious error in Danata"""
