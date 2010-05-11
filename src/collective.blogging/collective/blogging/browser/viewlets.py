from zope.component import getMultiAdapter
from five import grok
from zope.security import checkPermission
from collective.blogging.interfaces import IText, ITextMarker
from collective.blogging.interfaces import ILink, ILinkMarker
from collective.blogging.interfaces import IImage, IImageMarker
from collective.blogging.interfaces import IFile, IFileMarker
from collective.blogging.interfaces import IEvent, IEventMarker
from plone.app.layout.viewlets.interfaces import IAboveContentBody

class Text(grok.Viewlet):
    grok.name('collective.blogging.TextViewlet')
    grok.context(ITextMarker)
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContentBody)
    
    def update(self):
        self.text = IText(self.context).text.output
        self.editor = checkPermission('cmf.ModifyPortalContent', self.context)

class Link(grok.Viewlet):
    grok.name('collective.blogging.LinkViewlet')
    grok.context(ILinkMarker)
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContentBody)

    def update(self):
        self.remote_url = ILink(self.context).remote_url
        self.editor = checkPermission('cmf.ModifyPortalContent', self.context)

class Image(grok.Viewlet):
    grok.name('collective.blogging.ImageViewlet')
    grok.context(IImageMarker)
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContentBody)
    
    def update(self):
        self.picture = IImage(self.context).picture
        self.thumb = IImage(self.context).thumb
        self.editor = checkPermission('cmf.ModifyPortalContent', self.context)

class File(grok.Viewlet):
    grok.name('collective.blogging.FileViewlet')
    grok.context(IFileMarker)
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContentBody)
    
    def update(self):
        self.file = IFile(self.context).file
        self.editor = checkPermission('cmf.ModifyPortalContent', self.context)

class Event(grok.Viewlet):
    grok.name('collective.blogging.EventViewlet')
    grok.context(IEventMarker)
    grok.require('zope2.View')
    grok.viewletmanager(IAboveContentBody)

    def update(self):
        toLocalizedTime = getMultiAdapter((self.context, self.request), name=u'plone').toLocalizedTime
        start = IEvent(self.context).start
        end = IEvent(self.context).end
        self.start = start and toLocalizedTime(start.isoformat(), long_format=1) or None
        self.end = end and toLocalizedTime(end.isoformat(), long_format=1) or None
        self.editor = checkPermission('cmf.ModifyPortalContent', self.context)
