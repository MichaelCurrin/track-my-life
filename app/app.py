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
from lib import conf
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

# For implementation on PythonAnywhere.com:
# mount app directories as `app` object, as set in wsgi file.
start = True # main?

configfile = 'etc/cherrypy.conf'
# configDict={
#         'global':
#             {
#             #'environment':'embedded',
#             'socket_port': 9090,
#             },
#         }

# The script runs in the cloud PythonAnywhere.com by importing the `app` object and running it on the WSGI file. For all other uses, it is expected that this script will be run as the main file.
if __name__ == '__main__':
    cherrypy.log('Cherrypy Version: {}'.format(cherrypy.__version__))

    cherrypy.tree.mount(cherrypy.root, script_name='', config=configfile)
    # It's not working to set this in [global] under config file.
    cherrypy.server.socket_port = conf.getint('API', 'port')

    cherrypy.engine.start()
    cherrypy.engine.block()

else:
    app = cherrypy.Application(cherrypy.root, script_name='',
                               config='etc/cherrypy.conf')
