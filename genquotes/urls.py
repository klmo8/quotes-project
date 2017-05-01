from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^displaycs/$', views.displaycs, name='displaycs'),
    url(r'^displaystoic/$', views.displaystoic, name='displaystoic'),
    #url(r'^searchcs/(?P<author>[\w.@+-]+)/$', views.searchcs, name='searchcs'),
    url(r'^searchcs/$', views.searchcs, name='searchcs'),


    #url(r'^(?P<authorname>.*)/searchcs/$', views.searchcs, name='searchcs'),

    #url(r'^(?P<authorname>[\w.@+-]+)/searchcs/$', views.searchcs, name='searchcs'),
    #url(r'^searchcs/$', views.searchcs, name='searchcs'),

    #url(r'^(?P<authorname>)/searchcs/$', views.searchcs, name='searchcs'),




    #url(r'^(?P<quote_id>[0-9]+)/$', views.display, name='display'),
]
