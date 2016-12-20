from django.conf.urls import include, url
from django.contrib import admin
from dog import views
from paper import views as paper_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^paper/$', paper_views.paper_list),
    url(r'^author/$', paper_views.author_list),
    url(r'^admin/', include(admin.site.urls)),
]
