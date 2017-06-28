#!/usr/bin/env python2
"""
Test use of model.py as a sqlite database.

This script requires sqlobject library to be installed but sqlite is not needed.
Note also that sqlite cannot be installed in a virtual env due to an error that it must be at global level.

http://turbogears.org/1.0/docs/api/sqlobject.sresults.SelectResults-class.html
"""
from random import randint

from sqlobject import AND, OR

# Allow dirs in app to be imported.
import configureTests
from lib import database as db

# Create user to be used for record inserts.
user = db.User(username='tester')
# This should be 1 in development.
userID = user.id

print list(db.User.select())
print


#r = db.Record(userID=userID)

# Insert record in database (id increments)
# and make it available in this script.
for x in range(5):
    record = db.Mood(
        userID=userID,
        emotion=randint(-2,2),
        sadness=randint(0,3),
        joy=randint(0,3)
    )
    print record
print

# Print contents of DB
#print list(db.Mood.select())

#print db.Mood
# Print select statement
#print db.Mood.select()

'''


#print record.id
#print record.timestamp
print 'ALL'
print 'query'
print db.Mood.select()
print
print 'Values'
results = list(db.Mood.select())
for y in results:
    print y
print
print 'Count all'
print db.Mood.select().count()
print 'Options'
print dir(db.Mood.select())

print

print
print 'ID <= 3'
print db.Mood.select(db.Mood.q.id<=3)
print
print ' First only'
print db.Mood.select(db.Mood.q.id<=3)[0]
print
print 'Emotion positive'
print db.Mood.select(db.Mood.q.emotion>0)
print
print 'Emotion positive AND joy 2 or more'
x= db.Mood.select(AND(db.Mood.q.emotion>0,
                        db.Mood.q.joy>1)
                    )
if x:
    print x

## get specific ID
# db.Mood.get(2)

"""
accumulate', 'accumulateMany', 'accumulateOne', 'avg', 'clause', 'clauseTables',
'clone', 'connection', 'count', 'distinct', 'filter', 'getOne', 'lazyColumns',
'lazyIter', 'limit', 'max', 'min', 'newClause', 'ops', 'orderBy',
'queryForSelect', 'reversed', 'sourceClass', 'sum', 'tables', 'throughTo'
"""
print
print
print 'Emotion positive OR joy 2 or more'
print db.Mood.select(OR(db.Mood.q.emotion>0,
                        db.Mood.q.joy>1)
                    ).count()


'''
