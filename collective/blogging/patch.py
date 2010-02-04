from monkey import patch
from Products.CMFDefault.DiscussionItem import DiscussionItemContainer
from AccessControl import getSecurityManager
from AccessControl import Unauthorized

import logging
logger = logging.getLogger('collective.blogging')

@patch(DiscussionItemContainer.replyCount, "3cc1be53aa51ec26f6e93b44f8bfe2479356507d")
def replyCount(self, content_obj):
    """ How many replies do i have? """
    outer = self._getDiscussable( outer=1 )
    if content_obj == outer:
        validate = getSecurityManager().validate
        result = []
        for item in self._container.values():
            reply = item.__of__(self)
            try:
                if validate(self, self, reply.getId(), reply):
                    result.append(reply)
            except Unauthorized:
                pass
        return len(result)
    else:
        replies = content_obj.talkback.getReplies()
        return self._repcount( replies )

logger.warning('Patching Products.CMFDefault.DiscussionItem.DiscussionItemContainer (replyCount)')
DiscussionItemContainer.replyCount = replyCount