""" Tests
"""
import unittest

#from zope.testing import doctestunit
#from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

import eea.translations

class TestCase(ptc.PloneTestCase):
    """ Test case
    """
    class layer(PloneSite):
        """ Layer
        """
        @classmethod
        def setUp(cls):
            """ Setup
            """
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             eea.translations)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            """ Setup
            """
            pass


def test_suite():
    """ Suite
    """
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
            #'README.txt', package='eea.translations',
            #setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
            #module='eea.translations.mymodule',
            #setUp=testing.setUp, tearDown=testing.tearDown),

        # Integration tests that use PloneTestCase
        ztc.ZopeDocFileSuite(
            'README.txt', package='eea.translations',
            test_class=TestCase),

        #ztc.FunctionalDocFileSuite(
            #'browser.txt', package='eea.translations',
            #test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
