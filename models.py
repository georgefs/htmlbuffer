from google.appengine.ext import ndb, db

class TempFile(ndb.Model):
    url = ndb.StringProperty(indexed=False)
    html = ndb.StringProperty(indexed=False)
    updated = ndb.DateTimeProperty(auto_now=True)
