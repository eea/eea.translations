""" Base
"""
import eea.translations
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure

@onsetup
def setup_translations():
    """ Setup translations
    """
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', eea.translations)
    fiveconfigure.debug_mode = False

setup_translations()
PloneTestCase.setupPloneSite(extension_profiles=('eea.translations:default', ))

class EEATranslationsTestCase(PloneTestCase.FunctionalTestCase):
    """ Test case class used for functional translations tests.
    """
