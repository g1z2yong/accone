from django import http
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render
from django import forms

from  models import myurl

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
	return render(request, 'index.html',{'form':form})

def  account(request):
	return render(request, 'account.html')

def newurl(request):
	if request.method == 'POST':
		instance=myurl()
		instance.myurl=request.POST['myurl']
		instance.status='PK'
		instance.put()
	
	return HttpResponse("upload  OK")