# -*- coding: utf-8 -*-
"""
SQLite database model in SQLObject.
"""
import sqlobject as so

from connection import conn


class Base(so.SQLObject):
    """
    Template table for others to derive from.
    """
    _connection = conn


class User(Base):
    """
    Table of app users.
    """
    # A GUID used to uniquely identify this item across systems and on the
    # internet. Does alternateID also enforce unique?
    #guid = so.StringCol(notNull=True, default=UUID, unique=True, alternateID=True)
    # Username defaults to None/Null, but if set it must be unique.
    username = so.UnicodeCol(default=None, unique=True, length=31)
    # The time the user profile was created. Defaults to current time.
    created = so.DateTimeCol(default=so.DateTimeCol.now)


class Record(Base):
    """
    Template table for other record tables to derive from.
    """
    # Add a foreign key to id in User table.
    # This is user_id in SQL or userID in Python.
    user = so.ForeignKey('User')
    # The time the entry was is recorded for. Defaults to current time
    # if not set or set to None.
    timestamp = so.DateTimeCol(default=so.DateTimeCol.now)

    def _set_userID(self, userID):
        """
        Override default set method to enforce that the user ID exists in User
        table when a record entry is created.
        There may be a better way to do this with a contrainst or changing
        the foreign key creation.
        """
        try:
            User.get(userID)
        except so.SQLObjectNotFound:
            raise so.SQLObjectNotFound("Unable to create entry since user ID "
                "{0} is not in User table.".format(userID))
        else:
            self._SO_set_userID(userID)


class JSONData(Record):
    """
    Table to hold any form of data in JSON format.

    Todo: extract date from data if available and overwrite value in
        inherited timestamp column. Consider conversion of datatypes.
    """
    # Optional label to describe the area or topic or page the data was
    # submitted on.
    area = so.UnicodeCol(default='', length=31)
    data = so.JSONCol(default=None)


class Note(Record):
    """
    Record diary entries as text with short title and a longer note.
    """
    title = so.UnicodeCol(default='', length=31)
    note = so.UnicodeCol(default='', length=255)


class Mood(Record):
    """
    Table to hold mood data.
    """
    # Emotional score from -2 to +2.
    emotion = so.IntCol(default=0)

    # Eight key emotional areas.
    joy = so.IntCol(default=0)
    trust = so.IntCol(default=0)
    fear = so.IntCol(default=0)
    surprise = so.IntCol(default=0)
    sadness = so.IntCol(default=0)
    disgust = so.IntCol(default=0)
    anger = so.IntCol(default=0)
    anticipation = so.IntCol(default=0)

    def _set_emotion(self, value):
        """
        Enforce rule that emotion value must be an integer or of a type which
        can be parsed to integer.
        And must be -2, -1, 0, 1 or 2.
        """
        try:
            intValue = int(value)
        except TypeError:
            raise 'TypeError, Emotion score must be an integer.'

        assert -2<=intValue<=2, \
            'ValueError, Emotion score must be between -2 and +2.'

        self._SO_set_emotion(intValue)
