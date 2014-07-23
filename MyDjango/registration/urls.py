from django.conf.urls import patterns, url
from registration import views

urlpatterns = patterns('',
                       # ex: /registration/
                       url(r'^$', views.index, name='index'),
                       # ex: /registration/check/
                       url(r'^check/$', views.check, name='check_account'),
                       # ex: /registration/submit/
                       url(r'^submit/$', views.submit_account, name='submit_account'),
                       )
