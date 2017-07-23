from django.conf.urls import url

from . import views

urlpatterns = [
    # Note: 'name=' parameter is just a way to refer to the associated views from other parts of the app (templates, views, etc).
    url(r'^$', views.home, name='home'),
    url(r'^displaycs/$', views.displaycs, name='displaycs'),
    url(r'^displaystoic/$', views.displaystoic, name='displaystoic'),
    url(r'^searchcs/$', views.searchcs, name='searchcs'),


    #url(r'^(?P<authorname>.*)/searchcs/$', views.searchcs, name='searchcs'),

    #url(r'^(?P<authorname>[\w.@+-]+)/searchcs/$', views.searchcs, name='searchcs'),
    #url(r'^searchcs/$', views.searchcs, name='searchcs'),

    #url(r'^(?P<authorname>)/searchcs/$', views.searchcs, name='searchcs'),




    #url(r'^(?P<quote_id>[0-9]+)/$', views.display, name='display'),
]
