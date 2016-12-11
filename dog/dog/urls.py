from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'dog.views.index', name='index'),
    url(r'^index/$', 'dog.views.index', name='index'),
    url(r'^paper/$', 'paper.views.paper_list'),
    url(r'^author/$', 'paper.views.author_list'),
    url(r'^admin/', include(admin.site.urls)),
)
