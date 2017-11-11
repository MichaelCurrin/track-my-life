#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Track My Life server application file.

Run a Python server to serve HTML and allow REST API requests, so users can
log and read their personal activity in a browser.
"""
__author__ = '@MichaelCurrin'

import argparse
import os
import sys
#sys.stdout = sys.stderr

import cherrypy

from lib import APP_DIR, conf
from lib import database as db
from services import setupSERVICES


class Root(object):
    """
    Service for application root.
    """

    ## TEMP
    ## Leave this unexposed while in dev, so that we get a 404 on a bad path.
    ##@cherrypy.expose
    def default(self, *args, **kwargs):
        """
        For paths which do not exactly match the ui HTML pages, redirect to home page.
        """
        raise cherrypy.HTTPRedirect('/', 302)


def setup():
    """
    Main application setup.

    Read the log and http configuration files for the cherrypy app.
    Mount the web app and services app on the cherrypy tree and apply
    configuration to them.

    @return webApp: The application with web app and services app mounted.
    """
    for c in ('log.conf', 'log.local.conf', 'http.conf', 'http.local.conf'):
        path = os.path.join(APP_DIR, 'etc', c)
        if os.access(path, os.R_OK):
            cherrypy.config.update(path)

    cherrypy.log("Mounting application", context="SETUP")

    controllersConf = os.path.join(APP_DIR, 'etc', 'controllers.conf')
    controllersLocalConf = os.path.join(APP_DIR, 'etc',
                                        'controllers.local.conf')
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

    return webApp


def initialise(dropAll=False):
    """
    Main application initialisation.

    @return: None
    """
    db.initialise(dropAll=dropAll)


def run():
    """
    Read command-line arguments, setup web app and server, intililiase app
    and db and start the app.

    @return app: The application with web app and services app mounted. This
        is returned so that the app exists in the global space and can be
        imported into the WSGI script.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--drop',
                        action='store_true',
                        help="Boolean flag. If True, drop the entire db on app"
                            " start, then create tables. Default False.")

    args = parser.parse_args()

    # TODO:
    # - Daemonise
    # - PID
    # - user and log permissions

    app = setup()

    initialise(dropAll=args.drop)

    return app


# We can run the application on PythonAnywhere.com by importing this object
# into the WSGI script. In that case, we must not start or block the app.
app = run()


if __name__ == '__main__':
    cherrypy.engine.start()
    cherrypy.engine.block()
