# behaviours and markers
from collective.blogging.behaviours import IBlog, IBlogMarker
from collective.blogging.behaviours import IEntry, IEntryMarker
from collective.blogging.behaviours import IText, ITextMarker
from collective.blogging.behaviours import ILink, ILinkMarker
from collective.blogging.behaviours import IImage, IImageMarker
from collective.blogging.behaviours import IFile, IFileMarker
from collective.blogging.behaviours import IEvent, IEventMarker

# layers
from plone.theme.interfaces import IDefaultPloneLayer

class IBloggingSpecific(IDefaultPloneLayer):
    """ A marker interface that defines a Zope 3 browser layer. """
