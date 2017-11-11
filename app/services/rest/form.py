# -*- coding: utf-8 -*-
"""
Form handler.

For datetime conversion format see
    https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
"""
import datetime
import json

from lib import conf
from lib import database as db


class Form(object):
    """
    Handler for /services/rest/form/ endpoint.

    Include form name as /services/rest/form/{name} .

    This has been set in CherryPy config to return HTML instead of JSON, for
    thank you page. This might need to be setup differently for Analytics
    to be JSON if required.

    Todo: set accept content in etc as JSON instead of www form encode?
    """

    exposed = True

    # Read HTML templates from conf.
    dataOut = conf.get('HTML', 'dataOut')
    simplePage = conf.get('HTML', 'simplePage')

    def GET(self, name=None, *args, **kwargs):
        """
        Not used.
        """
        return name

    def POST(self, name=None, *args, **kwargs):
        """
        Insert data in the database and return either thank you message or
        received data.

        Todo: raise error or error page for missing or invalid data which is
        not covered by basic setup. Though validation can also happen on
        the form frontend side.
        Raise error if data could not inserted into inserted into db.
        Rethink user creation and possibly user ID from session,
        so user ID is not hardcoded. Unless user ID can be set fixed True/False
        in config and also database drop all to be reset.
        And actual test user id and username in initialise can be set in config.
        Possibly set user id in cherrypy.request.header with a tool
        so that it is passed on all requests and can be read along with data.
        Ask user to login/register otherwise.

        @param name: The name of the area to be tracked. Default to None.

        @keyword args: Values after the name in the URL as list.
        @keyword kwargs: Form field names and values as a dictionary.
        """
        # Remove timestamp from data if present and add to timestamp column,
        # otherwise use column's default value of now.
        datetimeStr = kwargs.pop('timestamp', None)
        if datetimeStr:
            datetimeFormat = '%Y-%m-%dT%H:%M'
            timestamp = datetime.datetime.strptime(datetimeStr, datetimeFormat)

            entry = db.JSONData(userID=1, area=name, data=kwargs,
                                timestamp=timestamp)
        else:
            entry = db.JSONData(userID=1, area=name, data=kwargs)

        #return self.dataOut.format(data=str(entry).replace('<','&lt')\
        #    .replace('>','&gt'))

        #dataStr = json.dumps(entry.data, indent=4)
        #return self.dataOut.format(data=dataStr)

        # Return HTML response as either data or simple page.
        thankYouData = conf.getboolean('Form', 'thankYouData')
        if thankYouData:
            dataDict = {'name': name, 'args': args, 'kwargs': kwargs}
            dataStr = json.dumps(dataDict, indent=4)
            resp = self.dataOut.format(data=dataStr)
        else:
            resp = self.simplePage.format(title='Thank You', h1='Thank You',
                message='Your results have been submitted.')
        return resp


class Analytics(object):
    """
    Handler for services/rest/form/analytics service.

    Set name as either services/rest/form/analytics/{name} or
    services/rest/form/analytics?name={name}.

    Get aggregated data out from database for the user.
    """

    exposed = True

    def GET(self, name=None, *args, **kwargs):
        if name:
            # Get all data for required table.
            query = """SELECT * FROM {0};""".format(name)
        else:
            # Get list of table names.
            query = """SELECT name FROM sqlite_master ORDER BY name ASC;"""
            # Convert tuple list to strings.

        res = db.conn.queryAll(query)

        # Convert tuples to lists.
        #res = [list(x) for x in res]

        # convert to string to allow JSON output to not create errors
        return str(res)


if __name__ == '__main__':
    print Analytics().GET('')
