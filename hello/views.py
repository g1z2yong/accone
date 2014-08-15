from django import http
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render
from django import forms

from  models import myurl,Account,Nodeall,Message

import datetime


class CommentForm(forms.Form):
    name = forms.CharField(
                widget=forms.TextInput(attrs={'class':'special'}))
    url = forms.URLField()
    comment = forms.CharField(
               widget=forms.TextInput(attrs={'size':'40'}))

def home(request):
    #return http.HttpResponse('Hello World! A')
	#return render(request, 'index.html')
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	instance=myurl(myurl="%s"%now,status='OK')
	instance.put()
	form = CommentForm(auto_id=False)
	accout= Account.query(Account.aid>0).fetch()
	message=Message.query().fetch()
	nodeall=Nodeall.query(Nodeall.ntemp=='T').fetch()
	total=dict(j=0,d=0)
	for node in nodeall:
		total['j']=total['j']+node.nd		
		total['d']=total['d']+node.nd
	return render(request, 'index.html',{'form':form,'acc':accout,'message':message,'nodeall':nodeall,'total':total})

def  account_page(request):
	if request.method == 'POST':
		aid=request.POST['aid']
		aname=request.POST['aname']
		accin= Account()
		accin.aid=int(aid)
		accin.aname=aname
		accin.put()
		return HttpResponseRedirect('/account')
	if request.method == 'GET':
		accout= Account.query(Account.aid>0).fetch()
		return render(request, 'account.html',{'acc':accout})

def  message(request):
	if request.method == 'GET':
		return render(request, 'message.html')

def newnode(request):
	if request.method == 'POST':
		node=Nodeall()
		node.naccid=int(request.POST['naccid'])
		node.nmessage=request.POST['nmessage']
		node.nj=float(request.POST['nj'])
		node.nd=float(request.POST['nd'])
		node.ntemp='T'
		node.put()
		if  'saveme' in request.POST:
			m=Message()
			m.message=request.POST['nmessage']
			m.put()
			#return HttpResponse(request.POST['saveme'])
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/')
	
	

def newurl(request):
	if request.method == 'POST':
		instance=myurl()
		instance.myurl=request.POST['myurl']
		instance.status='PK'
		instance.put()
	
	return HttpResponse("upload  OK")