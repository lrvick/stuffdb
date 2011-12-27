from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from main.views import add_thing, view_thing, edit_thing, list_things

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', add_thing),
    url(r'^list/$', list_things),
    url(r'^thing/(?P<lookup>\d+)$', view_thing),
    url(r'^thing/(?P<lookup>[-\w]+)$', view_thing),
    url(r'^thing/(?P<lookup>[-\w]+)/edit$', edit_thing),
)
