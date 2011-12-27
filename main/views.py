from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from main.models import Domain
from main.forms import ThingForm

#yeah same issue
#print out what obj is

def add_thing(request):
    domain, is_created = Domain.objects.get_or_create(name=request.get_host())
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save(commit=False)
            obj.domain = domain
            obj.save()
            return HttpResponseRedirect('/thing/%s' % cd['slug'])
    else:
        form = ThingForm()
        return render_to_response(
            'add_thing.html',
            {
                'form':form,
                'site_name':settings.SITE_NAME,
                'title':'Add Thing',
            },
            context_instance=RequestContext(request)
        )

def view_thing(request,slug):
    domain, is_created = Domain.objects.get_or_create(name=request.get_host())
    return render_to_response(
        'view_thing.html',
        {
            'site_name':settings.SITE_NAME,
            'title':'View thing',
        },
        context_instance=RequestContext(request)
    )

def list_things(request):
    domain, is_created = Domain.objects.get_or_create(name=request.get_host())
    return render_to_response(
        'view_thing.html',
        {
            'site_name':settings.SITE_NAME,
            'title':'List of things',
        },
        context_instance=RequestContext(request)
    )
