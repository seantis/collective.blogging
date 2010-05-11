from plone.namedfile.field import NamedBlobFile
from plone.namedfile.field import NamedBlobImage
from plone.app.textfield import RichText
from zope.interface import alsoProvides, Interface
from plone.directives import form
from zope import schema
from collective.blogging import _

class IBlog(form.Schema):
    """Blogging support for a folderish content
    """

    form.write_permission(page_size='collective.blogging.ModifyBlog')
    page_size = schema.Int(
        title=_(u'Page size'),
        description=_(u'Enter number of entries listed on the blog page.'),
        required=True,
        default=None,
        missing_value=None, # important!
    )

alsoProvides(IBlog, form.IFormFieldProvider)

class IBlogMarker(Interface):
    """Marker interface that will be provided by instances using the
    IBlog behavior.
    """

class IEntry(form.Schema):
    """Blogging support for a non-folderish content
    """

    form.write_permission(page_size='collective.blogging.ModifyEntry')
    is_entry = schema.Bool(
        title=_(u'Is entry'),
        required=True,
        default=True,
        readonly=True,
    )

alsoProvides(IEntry, form.IFormFieldProvider)

class IEntryMarker(Interface):
    """Marker interface that will be provided by instances using the
    IEntry behavior.
    """

class IEvent(form.Schema):
    """Event based blogging entry
    """

    form.write_permission(start='collective.blogging.ModifyEntry')
    start = schema.Datetime(
        title=_(u'Event start'),
        required=False,
        missing_value=None, # important!
    )
    
    form.write_permission(end='collective.blogging.ModifyEntry')
    end = schema.Datetime(
        title=_(u'Event end'),
        required=False,
        missing_value=None, # important!
    )

alsoProvides(IEvent, form.IFormFieldProvider)

class IEventMarker(Interface):
    """Marker interface that will be provided by instances using the
    IEvent behavior.
    """

class IFile(form.Schema):
    """Link based blogging entry
    """

    form.write_permission(file='collective.blogging.ModifyEntry')
    file = NamedBlobFile(
        title=_(u"File"),
        description=_(u"Please upload an file"),
        required=False,
    )

alsoProvides(IFile, form.IFormFieldProvider)

class IFileMarker(Interface):
    """Marker interface that will be provided by instances using the
    IFile behavior.
    """

class IImage(form.Schema):
    """Link based blogging entry
    """

    form.write_permission(picture='collective.blogging.ModifyEntry')
    picture = NamedBlobImage(
        title=_(u"Picture"),
        description=_(u"Please upload a picture"),
        required=False,
    )
    
    form.write_permission(thumb='collective.blogging.ModifyEntry')
    thumb = NamedBlobImage(
        title=_(u"Thumbnail"),
        readonly=True,
        required=False,
    )

alsoProvides(IImage, form.IFormFieldProvider)

class IImageMarker(Interface):
    """Marker interface that will be provided by instances using the
    IImage behavior.
    """

class ILink(form.Schema):
    """Link based blogging entry
    """

    form.write_permission(remote_url='collective.blogging.ModifyEntry')
    remote_url = schema.TextLine(
            title=_(u'Remote URL'),
            required=False,
            missing_value=None, # important!
        )

alsoProvides(ILink, form.IFormFieldProvider)

class ILinkMarker(Interface):
    """Marker interface that will be provided by instances using the
    ILink behavior.
    """

class IText(form.Schema):
    """Link based blogging entry
    """

    form.write_permission(text='collective.blogging.ModifyEntry')
    text = RichText(
            title=_(u'Text'),
            required=False,
            missing_value=None, # important!
        )

alsoProvides(IText, form.IFormFieldProvider)

class ITextMarker(Interface):
    """Marker interface that will be provided by instances using the
    IText behavior.
    """
