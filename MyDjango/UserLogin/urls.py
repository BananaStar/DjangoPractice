from django.conf.urls import patterns, url
from UserLogin import views

urlpatterns = patterns('',
                       # ex: /UserLogin/
                       url(r'^$', views.index, name='index'),
                       )
