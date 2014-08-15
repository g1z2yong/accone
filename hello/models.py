from google.appengine.ext import ndb

# Create your models here.

class myurl(ndb.Model):
	date = ndb.DateTimeProperty(auto_now=True)
	myurl = ndb.StringProperty()
	status = ndb.StringProperty()

class Account(ndb.Model):
	aid = ndb.IntegerProperty()
	aname = ndb.StringProperty()
	adetail = ndb.StringProperty()

class Nodeall(ndb.Model):
	nid = ndb.IntegerProperty()
	naccid = ndb.IntegerProperty()
	nmessage = ndb.StringProperty()
	nj = ndb.FloatProperty()
	nd = ndb.FloatProperty()
	ntemp = ndb.StringProperty()

	
class Message (ndb.Model):
	short = ndb.StringProperty()
	message=ndb.StringProperty()

class Mid:
	month=ndb.IntegerProperty()
	mid=ndb.IntegerProperty()
	