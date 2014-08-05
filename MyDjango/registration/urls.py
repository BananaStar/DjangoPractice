from django.conf.urls import patterns, url
from registration import views

urlpatterns = patterns('',
                       # ex: /registration/test/
                       url(r'^test/$', views.test, name='test'),
                       # ex: /registration/
                       url(r'^$', views.index, name='index'),
                       # ex: /registration/%user_account%
                       url(r'^(?P<user_account>\S+)/$', views.check_available, name='check_account'),
                       )
