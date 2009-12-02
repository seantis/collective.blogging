import logging
import transaction

from zope.interface import alsoProvides, noLongerProvides

from Products.CMFCore.utils import getToolByName

#BBB - see interfaces.py
from collective.blogging.interfaces import (IEntryMarker, IDocumentMarker,
                                            INewsItemMarker, IEventMarker,
                                            ILinkMarker, IImageMarker,
                                            IFileMarker)    

logger = logging.getLogger("collective.blogging")
PROFILE_ID = 'profile-collective.blogging:default'

#BBB - see interfaces.py
def fixEntryMarkup(context):
    logger.info("Starting migration of old blog entries markup to new one.")
    catalog = getToolByName(context, 'portal_catalog')
    ifaces = (IDocumentMarker, INewsItemMarker, IEventMarker, ILinkMarker,
                IImageMarker, IFileMarker)
    entry_brains = catalog(object_provides=[x.__identifier__ for x in ifaces])
    logger.info("Found %s blog enries with old markup.", len(entry_brains))
    for brain in entry_brains:
        try:
            entry = brain.getObject()
        except (AttributeError, KeyError):
            logger.warn("AttributeError getting entry object at %s",
                        brain.getURL())
            continue
        
        for iface in ifaces:
            if iface.providedBy(entry):
                noLongerProvides(entry, iface)
                logger.info('Markup "%s" removed from "%s".' % (iface.__identifier__,
                                                                brain.getPath()))
            
            if not IEntryMarker.providedBy(entry):
                alsoProvides(entry, IEntryMarker)
                logger.info('Markup "%s" set for "%s".' % (IEntryMarker.__identifier__,
                                                            brain.getPath()))
        
        logger.info("Committing transaction after migrating this entry.")
        transaction.commit()
