# -*- coding: utf-8 -*-
"""
Database initialisation and storage handling module.
"""
import json

import cherrypy

# Allow access to tables of models package as properties of database module.
from models import *
# Make connection available in database module.
# e.g. database.conn.queryAll(statement)
# e.g. database.conn.queryOne(statement)
from models.connection import conn

# Todo: move to app.conf
DEFAULTS_FILE = 'lib/' + 'defaultData.json'


def initialise(createAll=True, dropAll=False):
    """
    Initialise the database tables and setup default data. All tables
    may be dropped with parameter dropAll.

    Will create any new tables that does not already exist and possibly
    recreating those that already exist based on the values of L{createAll} and
    L{dropAll}.

    @param createAll: If B{True} (default), any tables that do not already exist
        will be created.
    @type createAll: bool
    @param dropAll: If B{True} (default is B{False}), all existing tables will
        be dropped first before they are created again if required.
    @type dropAll: bool
    """
    modelsList = []

    # Get names.
    import models as ml

    for m in ml.__all__:
        mo = getattr(ml, m)
        modelsList.append(mo)

    # Drop tables.
    if dropAll:
        for m in modelsList:
            cherrypy.log("Dropping %s" % m.__name__, 'DATABASE.INIT')
            m.dropTable(ifExists=True, dropJoinTables=True, cascade=True)

    # Create tables.
    # Todo: see Piccing database.py for how to deal with contraints here.
    if createAll:
        for m in modelsList:
            cherrypy.log("Creating %s" % m.__name__, 'DATABASE.INIT')
            m.createTable(ifNotExists=True)

    # Populate appropriate tables with the required default data.
    #defaultData()

    # Create default user if does not already exist.
    if not ml.User.selectBy(id=1).count():
        ml.User(id=1, username='michaelcurrin')


def defaultData():
    """
    This method ensures that the following tables contain the appropriate data:
        - ...
        - ...

    NOTE: This method will only populate an empty table. If the relevant table
    contains any data, it will be ignored.
    """
    with open(DEFAULTS_FILE) as dataFile:
        data = json.load(dataFile)

    # Insert all the XXX types, if not yet defined.
    '''
    if E6dType.select().count() == 0:
        e6dTypes = [
            {"listOrder": 10, "name": u"Product"},
            {"listOrder": 20, "name": u"Article"},
            {"listOrder": 30, "name": u"Video"},
        ]

        for record in e6dTypes:
            logger(
                "Inserting Enriched Types (E6D) record: {0}".format(record),
                context="LIB.DATABASE.DEFAULTDATA"
            )
            # Create the record by passing the data to the model
            E6dType(**record)
    '''
    # To be decided: Memories should be copied from Goals or Lessons
    # or as a new section of its own.

if __name__ == '__main__':
    # Notes on queries
    res = conn.queryAll("SELECT * FROM User")
    print res
    res = conn.queryOne("SELECT id FROM User")
    print res

    # Test that data is formatted correctly and print it out.
    # $ python -m lib.database
    with open(DEFAULTS_FILE) as dataFile:
        data = json.load(dataFile)
    print json.dumps(data, indent=4, sort_keys=True)
