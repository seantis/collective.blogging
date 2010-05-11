from plone.namedfile import NamedBlobImage
from collective.blogging.interfaces import IImage
from collective.blogging.interfaces import IImageMarker
from collective.blogging.utils import scaleImage
from five import grok
from zope.app.container.interfaces import IObjectAddedEvent
from zope.lifecycleevent.interfaces import IObjectModifiedEvent

from logging import getLogger
log = getLogger('collective.blogging')

def scalePicture(obj):
    picture = IImage(obj).picture
    if picture is not None:
        thumbnail = scaleImage(picture.data, 200, 200)
        # FIXME: height and width attributes are -1 - we need to find those attributes for template usage
        IImage(obj).thumb = NamedBlobImage(thumbnail, filename=u'%s (thumb)' % picture.filename)
    
# Subscribers
@grok.subscribe(IImageMarker, IObjectAddedEvent)
def scaleImages(obj, event):
    try:
        scalePicture(obj)
    except IOError, e:
        import pdb; pdb.set_trace( )
        log.info('Looks like a scaling support is missing: %s' % str(e))

@grok.subscribe(IImageMarker, IObjectModifiedEvent)
def reScaleImages(obj, event):
    try:
        scalePicture(obj)
    except IOError, e:
        log.info('Looks like a scaling support is missing: %s' % str(e))
