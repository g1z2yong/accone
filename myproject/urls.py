from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'hello.views.home'),
	url(r'^newurl', 'hello.views.newurl'),
	url(r'^account', 'hello.views.account'),
)