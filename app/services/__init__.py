# -*- coding: utf-8 -*-
"""
Services module.
"""
__all__ = ['setupSERVICES']

import cherrypy

from lib import conf
from rest import setupREST


class Services(object):
    """
    Handler for Services service as base/services/ .
    """

    def __init__(self):
        """
        Use this for testing purposes.
        """
        self.html = conf.get('HTML', 'simplePage').format(title='Services',
            h1='Services', message='')

    @cherrypy.expose
    def index(self):
        """Return HTML file which was python formatted on startup."""
        return self.html


def setupSERVICES():
    """
    Create Services instance and add other instances to it.

    @return services: instance of Services, with rest added as attribute.
    """

    services = Services()
    services.rest = setupREST()

    return services
