from google.appengine.ext import ndb

# Create your models here.

class myurl(ndb.Model):
	date = ndb.DateTimeProperty(auto_now=True)
	myurl = ndb.StringProperty()
	status = ndb.StringProperty()