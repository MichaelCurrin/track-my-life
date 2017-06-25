#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Web base application for HTML frontend and python RESST API, intended for
logging and journaling of personal details.
"""
__author__ = '@MichaelCurrin'
__version__ = '1.0'

import sys
# From a PythonAnywhere cherrypy tutorial.
sys.stdout = sys.stderr

import cherrypy

# Be careful when testing this line alone in python command line, as you are
# working in '__main__' and the script will be imported as '__main__'.
from lib import database as db

### TO BE REMOVED
# For development, start with fresh tables each time app is reloaded,
db.initialise(dropAll=True)
# Once the database is stable, the line should be removed.
# then any changes in classes will be recognised in python when app reloads
# but changes to DB will have to be done with update script written in SQL.
# (or use SQLObject with add/remove column etc. if it allows it)

# Build Services API.
from services import setupSERVICES


class Root(object):
    """
    Appication root as base/ or base/ui/index.html
    """
    @cherrypy.expose
    def index(self):
        """
        Static home page.
        """
        return file('ui/index.html')


cherrypy.root = Root()
cherrypy.root.services = setupSERVICES()

# Test how this appears in PythonAnywhere log, vs doing a print.
# Also test the stdout setting at the top.
cherrypy.log('Mounting app')

# Mount app directories as `app` object, as set in wsgi file
app = cherrypy.Application(cherrypy.root, script_name='',
                           config='etc/cherrypy.conf')

# Add quickstart here for testing off PythonAnywhere?
# if main? see my flask app.

cherrypy.log('Starting app')
cherrypy.log('Engine state: {}'.format(cherrypy.engine.state))
cherrypy.log('Version: {}'.format(cherrypy.__version__))
