from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from main.views import add_thing, view_thing

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$/', add_thing),
    url(r'^thing/(?P<slug>\w+)$', view_thing),
)
