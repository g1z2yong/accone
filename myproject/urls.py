from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'hello.views.home'),
	url(r'^newurl', 'hello.views.newurl'),
	url(r'^account', 'hello.views.account_page'),
	url(r'^message', 'hello.views.message'),
	url(r'^newnode', 'hello.views.newnode'),
)