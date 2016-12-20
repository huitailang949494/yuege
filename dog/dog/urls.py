from django.conf.urls import include, url
from django.contrib import admin
from dog import views
import paper

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    # url(r'^paper/$', paper.views.paper_list),
    # url(r'^author/$', paper.views.author_list),
    url(r'^admin/', include(admin.site.urls)),
]
