from zope.publisher.interfaces.browser import IDefaultBrowserLayer
#from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultBrowserLayer):
    """Marker interface that defines a Zope 3 skin layer.
    """
