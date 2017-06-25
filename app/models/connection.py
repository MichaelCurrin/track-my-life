# -*- coding: utf-8 -*-
"""
Setup connection to database.

Alternatively, see approach in docs:
    http://sqlobject.org/SQLObject.html#declaring-a-connection
"""
from sqlobject.sqlite import builder
# todo: move to config file
DB_NAME = 'logger.db'

# Create connection to database to be shared by table classes.
conn = builder()(DB_NAME)
