#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Web base application for HTML frontend and python REST API, intended for
logging and journaling of personal details.
"""
__author__ = '@MichaelCurrin'

import sys
# From a PythonAnywhere cherrypy tutorial.
sys.stdout = sys.stderr

import cherrypy

# Be careful when testing this line alone in python command line, as you are
# working in '__main__' and the script will be imported as '__main__'.
from lib import database as db

### TO BE REMOVED
# For development phase, start with fresh tables each time app is reloaded,
db.initialise(dropAll=True)
# Once the database is stable, the line should be removed.
# then any changes in classes will be recognised in python when app reloads
# but changes to DB will have to be done with update script written in SQL.
# (or use SQLObject with add/remove column etc. if it allows it)
###

# Build Services API.
from services import setupSERVICES


class Root(object):
    """
    Service for application root as baseURI/ or baseURI/ui/index.html
    """
    @cherrypy.expose
    def index(self):
        """
        Static home page.
        """
        return file('ui/index.html')


cherrypy.root = Root()
cherrypy.root.services = setupSERVICES()

cherrypy.log('Mounting app')

# For implementation on PythonAnywhere.com,
# mount app directories as `app` object, as set in wsgi file.
app = cherrypy.Application(cherrypy.root, script_name='',
                           config='etc/cherrypy.conf')

cherrypy.log('Starting app')
cherrypy.log('Engine state: {}'.format(cherrypy.engine.state))
cherrypy.log('Version: {}'.format(cherrypy.__version__))
