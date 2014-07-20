from django.conf.urls import patterns, url
from Subscription import views

urlpatterns = patterns('',
                       # ex: /Subscription/
                       url(r'^$', views.index, name='index'),
                       # ex: /Subscription/check/
                       url(r'^check/$', views.check, name='checkAAA'),
                       )
