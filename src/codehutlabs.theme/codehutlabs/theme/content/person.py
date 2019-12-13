"""Definition of the Person content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from codehutlabs.theme import codehutlabsThemeMessageFactory as _

from codehutlabs.theme.interfaces import IPerson
from codehutlabs.theme.config import PROJECTNAME

PersonSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'hello_name',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Hello Name"),
            description=_(u"Hello Name Desc"),
        ),
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

PersonSchema['title'].storage = atapi.AnnotationStorage()
PersonSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(PersonSchema, moveDiscussion=False)


class Person(base.ATCTContent):
    """Simple Person Content Type"""
    implements(IPerson)

    meta_type = "Person"
    schema = PersonSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    hello_name = atapi.ATFieldProperty('hello_name')


atapi.registerType(Person, PROJECTNAME)
