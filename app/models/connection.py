# -*- coding: utf-8 -*-
"""
Setup connection to database.

Alternatively, see approach in docs:
    http://sqlobject.org/SQLObject.html#declaring-a-connection
"""
from sqlobject.sqlite import builder

from lib import conf


def setupConnection():
    """
    Create connection to database, to be shared by table classes. The file
    will be created if it does not exist.
    """
    dbPath = conf.get('db', 'path')
    conn = builder()(dbPath)

    return conn


conn = setupConnection()
