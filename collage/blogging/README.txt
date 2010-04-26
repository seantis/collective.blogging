
When collective.collage.blogging is installed dependencies are installed,

    >>> 'collective.collage.blogging' in [i['title'] for i in portal.portal_quickinstaller.listInstalledProducts()]
    True
    >>> 'collective.blogging' in [i['title'] for i in portal.portal_quickinstaller.listInstalledProducts()]
    True

    >>> #self.ipython(locals())

XXX: fix this...
    >>> 'Collage' in [i['title'] for i in portal.portal_quickinstaller.listInstalledProducts()]
    True

