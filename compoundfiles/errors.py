#!/usr/bin/env python
# vim: set et sw=4 sts=4 fileencoding=utf-8:
#
# A library for reading Microsoft's OLE Compound Document format
# Copyright (c) 2014 Dave Hughes <dave@waveform.org.uk>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import (
    unicode_literals,
    absolute_import,
    print_function,
    division,
    )
str = type('')


class CompoundFileError(IOError):
    """
    Base class for exceptions arising from reading compound documents.
    """

class CompoundFileInvalidMagicError(CompoundFileError):
    """
    Error raised when a compound document has an invalid magic number.
    """

class CompoundFileInvalidBOMError(CompoundFileError):
    """
    Error raised when a compound document is anything other than little-endian.
    """

class CompoundFileVersionError(CompoundFileError):
    """
    Error raised when the library version of a compound document isn't recognized.
    """


class CompoundFileWarning(Warning):
    """
    Base class for warnings arising from reading compound documents.
    """

class CompoundFileHeaderWarning(CompoundFileWarning):
    """
    Base class for warnings about header attributes.
    """

class CompoundFileSectorSizeWarning(CompoundFileHeaderWarning):
    """
    Base class for warnings about strange sector sizes in compound documents.
    """

