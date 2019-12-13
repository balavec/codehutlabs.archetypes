from codehutlabs.theme import codehutlabsThemeMessageFactory as _
from plone.theme.interfaces import IDefaultPloneLayer
from zope import schema
from zope.interface import Interface


class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer and a plone skin marker.
    """


class IPerson(Interface):
    """Simple Person Content Type"""

    # -*- schema definition goes here -*-
    hello_name = schema.TextLine(
        title=_(u"Hello Name"),
        required=False,
        description=_(u"Hello Name Desc"),
    )

