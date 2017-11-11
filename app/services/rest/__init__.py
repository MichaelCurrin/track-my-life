# -*- coding: utf-8 -*-
"""
Rest module.
"""
__all__ = ['setupREST']

from form import Form, Analytics


class Rest(object):
    """
    Handler for REST service.
    """

    exposed = True

    def GET(self, *args, **kwargs):
        return 'GET REST'


def setupREST():
    """
    Create Rest instance with other services added to it.
    """

    rest = Rest()
    rest.form = Form()
    rest.form.analytics = Analytics()

    #rest.test.mood = Mood()
    #rest.test.test3 = Test3()
    #rest.test.user = User()
    return rest
