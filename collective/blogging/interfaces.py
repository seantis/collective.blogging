from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer

# markers
class IBlogMarker(Interface):
    """ A content which can act like a blog """

class IFolderMarker(IBlogMarker):
    """ A blog folderish content """

class IEntryMarker(Interface):
    """ A generic blog entry """

class IDocumentMarker(IEntryMarker):
    """ A document based blog entry """

class INewsItemMarker(IEntryMarker):
    """ A news item based blog entry """

class IEventMarker(IEntryMarker):
    """ An event based blog entry """

class ILinkMarker(IEntryMarker):
    """ A link based blog entry """

class IImageMarker(IEntryMarker):
    """ An image based blog entry """

class IFileMarker(IEntryMarker):
    """ An file based blog entry """

class IBloggingSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """
