from Acquisition import aq_inner
from Acquisition import aq_base
from zope.component import getMultiAdapter
from plone.directives import dexterity
from zope.publisher.interfaces import IPublishTraverse, NotFound
from plone.namedfile.utils import set_headers, stream_data
from five import grok
from collective.blogging.interfaces import IBlogMarker
from collective.blogging.interfaces import IEntryMarker
from collective.blogging.interfaces import IImage, IImageMarker
from collective.blogging.interfaces import IBloggingSpecific

class Blog(dexterity.DisplayForm):
    grok.name(u'view')
    grok.context(IBlogMarker)
    grok.require(u'zope2.View')
    grok.layer(IBloggingSpecific)
    
    def buildQuery(self):
        context = aq_inner(self.context)
        path = '/'.join(context.getPhysicalPath())
        query = {
            'object_provides': IEntryMarker.__identifier__,
            'path'           : path
        }
        return query

    def contents(self):
        catalog = getMultiAdapter((self.context, self.request), name=u'plone_tools').catalog()
        query = self.buildQuery()
        return catalog(**query)

class Entry(dexterity.DisplayForm):
    grok.name(u'view')
    grok.context(IEntryMarker)
    grok.require(u'zope2.View')
    grok.layer(IBloggingSpecific)

    def macros(self):
        return self._template.macros

    def is_entry(self):
        return IEntryMarker.providedBy(self.context)

class Download(grok.CodeView):
    """Download a file, via ../context/@@download/fieldname/filename
    
    `fieldname` is the name of an attribute on the context that contains
    the file. `filename` is the filename that the browser will be told to
    give the file. If not given, it will be looked up from the field.
    
    The attribute under `fieldname` should contain a named (blob) file/image
    instance from this package.
    
    Taken from plone.namedfile and adapted for image behaviour.
    """
    
    grok.context(IImageMarker)
    grok.require('zope2.View')
    grok.implements(IPublishTraverse)
    
    def __init__(self, context, request):
        super(Download, self).__init__(context, request)
        self.fieldname = None

    def publishTraverse(self, request, name):
        
        if self.fieldname is None:  # ../@@download/fieldname
            self.fieldname = name
        else:
            raise NotFound(self, name, request)
        return self

    def __call__(self):
        # Ensure that we have a filedname
        if not self.fieldname:
            raise NotFound(self, '', self.request)
        
        file = getattr(IImage(aq_base(self.context)), self.fieldname)
        if file is None:
            raise NotFound(self, self.fieldname, self.request)
        
        filename = getattr(file, 'filename', None)
        set_headers(file, self.request.response, filename=filename)
        return stream_data(file)

    def render(self):
        return None