from lib import database as db

# Consider rewriting these as handlers in services.res.form or app.lib
# rather than as API

class User(object):
    """
    Endpoint for services/rest/form/user
    """

    # Consider where userID can be set when arriving on site
    # as registration. Or tempory value from random number.
    # Either way this can be stored in cherrypy session or cherrypy.response.cookie
    # so it is added to every request (though there would be a valid cookie
    # plus user name or user ID.
    exposed = True

    def GET(self, *args, **kwargs):
        """
        todo: check for id in args or kwargs
        db.selectBy(id=x)
        """
        users = list(db.User.select())
        # Convert to JSON.
        response = [dict(id=u.id, username=u.username, created=str(u.created)) \
            for u in users]
        return response

class Mood(object):
    """
    Endpoint for services/rest/form/mood
    """

    exposed = True

    def GET(self, *args, **kwargs):
        """
        Get data from the Mood table.
        """
        return list(db.Mood.select()) #{'args': args, 'kwargs': kwargs}
        #results = list(db.Mood.select())
        #return results

    def POST(self, param=None, *args, **kwargs):
        """
        Insert data in the Mood table.
        """
        record = db.Mood(userID=1, emotion=0)
        return {'param': param, 'args': args, 'kwargs': kwargs, 'record': record}


class Test3(object):
    exposed = True

    #@cherrypy.tools.json_out()
    def GET(self, *args, **kwargs):
        """
        """
        return ['some', 'data']

    def POST(self, length=8, *args, **kwargs):

        return {"length": length,
            "args": args,
            "kwargs": kwargs,
            }
