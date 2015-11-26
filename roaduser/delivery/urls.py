from django.conf.urls import patterns, url
from delivery import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^routes/$', views.routes, name='routes'),
    url(r'^add_route/$', views.add_route, name='add_route'),
    url(r'^add_item/$', views.add_item, name='add_item'),
    url(r'^items/$', views.items, name='items'),
    url(r'^about/$', views.about, name='about'),
    url(r'^items/pending/$', views.pending, name='pending'),
    )
