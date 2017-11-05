#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Track My Life server application file.

Run a Python server to serve HTML and allow REST API requests, so users can
log and read their personal activity in a browser.
"""
__author__ = '@MichaelCurrin'

import os
import sys
# From a PythonAnywhere cherrypy tutorial.
# TODO: This might send stdout to PA error logs - this could be removed
# once own log files are implemented.
sys.stdout = sys.stderr

import cherrypy

# Be careful when testing this line alone in python command line, as you are
# working in '__main__' and the script will be imported as '__main__'.
from lib import APP_DIR, conf
from lib import database as db
from services import setupSERVICES


class Root(object):
    """
    Service for application root.
    """

    ## TEMP
    ## Leave this unexposed while in def, so that we get a 404 on a bad path.
    ##@cherrypy.expose
    def default(self, *args, **kwargs):
        """
        For paths which do not exactly match the ui HTML pages, redirect to home page.
        """
        raise cherrypy.HTTPRedirect('/', 302)


# Only keep dropAll=True while in develop mode, to replace tables each time
# but also delete all data.
db.initialise(dropAll=True)

controllersConf = os.path.join(APP_DIR, 'etc', 'controllers.conf')
controllersLocalConf = os.path.join(APP_DIR, 'etc', 'controllers.local.conf')
servicesConf = os.path.join(APP_DIR, 'etc', 'services.conf')
servicesLocalConf = os.path.join(APP_DIR, 'etc', 'services.local.conf')

webApp = cherrypy.tree.mount(Root(), '/', config=controllersConf)
servicesApp = cherrypy.tree.mount(setupSERVICES(), '/services',
                                  config=servicesConf)

# If local config files exist, merge in the tree-specific sections for
# the appropriate app.
if os.access(controllersLocalConf, os.R_OK):
    webApp.merge(controllersLocalConf)
if os.access(servicesLocalConf, os.R_OK):
    servicesApp.merge(servicesLocalConf)

for c in ('http.conf', 'http.local.conf'):
    path = os.path.join(APP_DIR, 'etc', c)
    if os.access(path, os.R_OK):
        cherrypy.config.update(path)

# We can run the application on PythonAnywhere.com by importing this object
# into the WSGI script.
app = webApp

if __name__ == '__main__':
    cherrypy.engine.start()
    cherrypy.engine.block()
