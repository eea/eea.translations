""" Tests
"""

from Products.Five import fiveconfigure
from Products.Five import zcml
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
from Testing import ZopeTestCase as ztc
import eea.translations
import unittest

ptc.setupPloneSite()

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
        #doctestunit.DocFileSuite('README.txt',
                                 #package='eea.translations',
                                 #setUp=testing.setUp,
                                 #tearDown=testing.tearDown),
        #doctestunit.DocTestSuite(module='eea.translations.mymodule',
                                 #setUp=testing.setUp,
                                 #tearDown=testing.tearDown),
        ztc.ZopeDocFileSuite('README.txt',
                             package='eea.translations',
                             test_class=TestCase),
        #ztc.FunctionalDocFileSuite('browser.txt',
                                   #package='eea.translations',
                                   #test_class=TestCase),
        ])
