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
# From a PythonAnywhere cherrypy tutorial. TODO confirm how this works
# with own logs vs PythonAnywhere logs and also the fact the log.screen is
# set to False by using embedded mode.
sys.stdout = sys.stderr

import cherrypy

# Be careful when testing this line alone in python command line, as you are
# working in '__main__' and the script will be imported as '__main__'.
from lib import conf
from lib import database as db
from services import setupSERVICES


CONFIG_FILES = ('etc/cherrypy.conf', 'etc/cherrypy.local.conf')


class Root(object):
    """
    Service for application root.
    """
    @cherrypy.expose
    def index(self):
        """
        Static home page.

        TODO: Serve this and other pages off of root using the conf rather,
        without ui in path.
        """
        return file('ui/index.html')


# Only keep dropAll=True while in develop mode, to replace tables each time
# but also delete all data.
db.initialise(dropAll=True)

cherrypy.root = Root()
cherrypy.root.services = setupSERVICES()

for c in CONFIG_FILES:
    if os.access(c, os.R_OK):
        cherrypy.config.update(c)

# We can run the application on PythonAnywhere.com by importing this object
# into the WSGI script.
app = cherrypy.Application(cherrypy.root)


if __name__ == '__main__':
    cherrypy.engine.start()
    cherrypy.engine.block()
