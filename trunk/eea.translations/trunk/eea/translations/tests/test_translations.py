""" Doc tests
"""
import doctest
import unittest
from eea.translations.tests.base import EEATranslationsTestCase
from Testing.ZopeTestCase import FunctionalDocFileSuite

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

def test_suite():
    """ Suite
    """
    return unittest.TestSuite((
            FunctionalDocFileSuite('installation.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.translations.tests',
                  test_class=EEATranslationsTestCase),
            ))
