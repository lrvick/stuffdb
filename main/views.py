from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def add_thing(request):
    return render_to_response(
        'add_thing.html',
        {
            'site_name':settings.SITE_NAME,
            'title':'Add Thing',
        },
        context_instance=RequestContext(request)
    )

def view_thing(request,slug):
    return render_to_response(
        'view_thing.html',
        {
            'site_name':settings.SITE_NAME,
            'title':'View thing',
        },
        context_instance=RequestContext(request)
    )

def list_things(request):
    return render_to_response(
        'view_thing.html',
        {
            'site_name':settings.SITE_NAME,
            'title':'List of things',
        },
        context_instance=RequestContext(request)
    )
