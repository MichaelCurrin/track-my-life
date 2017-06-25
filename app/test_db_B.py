#!/usr/bin/env python2
"""
Test use of model.py as a sqlite database.
"""
from lib import database as db

d1 = range(100)
d2 = dict(a=1, b=2, c=3)
d3 = 'string'
d4 = [dict(x=100), dict(y=200, z=300)]

# Create data entries for user 1.
r1 = db.JSONData(userID=1, data=d1)
r2 = db.JSONData(userID=1, data=d2)
r3 = db.JSONData(userID=1, data=d3)
r4 = db.JSONData(userID=1, data=d4)

# working with conn
res = db.conn.queryAll("SELECT * FROM User")
print res
res = db.conn.queryOne("SELECT id FROM User")
print res

print list(db.JSONData.select())

# ipython -i test_db_B.py
"""
In [2]: r4.
r4.SelectResultsClass   r4.createIndexesSQL     r4.delete               r4.expire               r4.selectBy             r4.syncUpdate
r4.area                 r4.createJoinTables     r4.deleteBy             r4.get                  r4.set                  r4.tableExists
r4.childName            r4.createJoinTablesSQL  r4.deleteMany           r4.id                   r4.setConnection        r4.tablesUsedImmediate
r4.clearTable           r4.createTable          r4.destroySelf          r4.j                    r4.sqlmeta              r4.timestamp
r4.coerceID             r4.createTableSQL       r4.dropJoinTables       r4.q                    r4.sqlrepr              r4.user
r4.createIndexes        r4.data                 r4.dropTable            r4.select               r4.sync                 r4.userID

In [3]: r4.user
Out[3]: <User 1 username=u'michaelcurrin' created='datetime.datetime...)'>
In [4]: r4.userID
Out[4]: 1

In [5]: r4._
r4._SO_class_User              r4._SO_set_area                r4.__format__                  r4._connection
r4._SO_cleanDeprecatedAttrs    r4._SO_set_data                r4.__ge__                      r4._create
r4._SO_createValues            r4._SO_set_timestamp           r4.__getattribute__            r4._findAlternateID
r4._SO_depends                 r4._SO_set_user                r4.__getstate__                r4._getJoinsToCreate
r4._SO_fetchAlternateID        r4._SO_set_userID              r4.__gt__                      r4._get_area
r4._SO_finishCreate            r4._SO_setupSqlmeta            r4.__hash__                    r4._get_data
r4._SO_finishedClassCreation   r4._SO_to_python_area          r4.__init__                    r4._get_timestamp
r4._SO_foreignKey              r4._SO_to_python_data          r4.__le__                      r4._get_user
r4._SO_from_python_area        r4._SO_to_python_timestamp     r4.__lt__                      r4._get_userID
r4._SO_from_python_data        r4._SO_to_python_userID        r4.__module__                  r4._inheritable
r4._SO_from_python_timestamp   r4._SO_val_area                r4.__ne__                      r4._init
r4._SO_from_python_userID      r4._SO_val_data                r4.__new__                     r4._notifyFinishClassCreation
r4._SO_getID                   r4._SO_val_timestamp           r4.__reduce__                  r4._parent
r4._SO_getValue                r4._SO_val_userID              r4.__reduce_ex__               r4._reprItems
r4._SO_get_area                r4._SO_validatorState          r4.__repr__                    r4._set_area
r4._SO_get_data                r4._SO_writeLock               r4.__setattr__                 r4._set_data
r4._SO_get_timestamp           r4.__class__                   r4.__setstate__                r4._set_timestamp
r4._SO_get_user                r4.__classinit__               r4.__sizeof__                  r4._set_user
r4._SO_get_userID              r4.__delattr__                 r4.__sqlrepr__                 r4._set_userID
r4._SO_loadValue               r4.__dict__                    r4.__str__
r4._SO_selectInit              r4.__doc__                     r4.__subclasshook__
r4._SO_setValue                r4.__eq__                      r4.__weakref__


[5]: r4.__
r4.__class__         r4.__doc__           r4.__getattribute__  r4.__init__          r4.__ne__            r4.__repr__          r4.__sqlrepr__
r4.__classinit__     r4.__eq__            r4.__getstate__      r4.__le__            r4.__new__           r4.__setattr__       r4.__str__
r4.__delattr__       r4.__format__        r4.__gt__            r4.__lt__            r4.__reduce__        r4.__setstate__      r4.__subclasshook__
r4.__dict__          r4.__ge__            r4.__hash__          r4.__module__        r4.__reduce_ex__     r4.__sizeof__        r4.__weakref__

# Take note of:
r4.clearTable
All the `_SO_get_...` methods
"""
