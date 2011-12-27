from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

def add_thing(request):
    title = 'Add Thing'
    return render_to_response(
        'add_thing.html',
        {
            'site_name':settings.SITE_NAME,
            'title':title,
        },
        context_instance=RequestContext(request)
    )

def view_thing(request):
    title = 'View Thing'
    return render_to_response(
        'view_thing.html',
        {
            'site_name':settings.SITE_NAME,
            'title':title,
        },
        context_instance=RequestContext(request)
    )
