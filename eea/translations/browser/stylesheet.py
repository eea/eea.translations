import os
from Globals import DTMLFile

from Products.Five.browser import BrowserView


this_dir = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(this_dir, 'stylesheets')
logo_dtml = DTMLFile('logo.css', templates_dir)


class EEALogos(BrowserView):

    def __call__(self, *args, **kw):
	"""This view is published"""
	template = logo_dtml.__of__(self.context)
	return template(context=self.context)
