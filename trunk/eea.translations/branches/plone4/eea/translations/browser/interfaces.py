""" Interfaces
"""
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class IThemeSpecific(IDefaultBrowserLayer):
    """Marker interface that defines a Zope 3 skin layer.
    """
