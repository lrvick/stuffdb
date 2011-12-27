from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from main.views import add_thing, view_thing, edit_thing, list_things, serialize_thing, serialize_things

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', add_thing),
    url(r'^list/$', list_things),
    url(r'^serialize/(?P<markup>[-\w]+)$', serialize_things),
    url(r'^thing/(?P<lookup>\d+)$', view_thing),
    url(r'^thing/(?P<lookup>\d+)/edit$', edit_thing),
    url(r'^thing/(?P<lookup>\d+)/serialize/(?P<markup>[-\w]+)$', serialize_thing),
    url(r'^thing/(?P<lookup>[-\w]+)$', view_thing),
    url(r'^thing/(?P<lookup>[-\w]+)/edit$', edit_thing),
    url(r'^thing/(?P<lookup>[-\w]+)/serialize/(?P<markup>[-\w]+)$', serialize_thing),
)
