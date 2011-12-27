from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.defaultfilters import slugify
from django.http import HttpResponseRedirect
from django.conf import settings
from main.models import Domain, Thing
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
            return HttpResponseRedirect('/thing/%s' % slugify(cd['name']))
    else:
        form = ThingForm()
        return render_to_response(
            'add_thing.html',
            {
                'form':form,
                'site_name':settings.SITE_NAME,
                'things': Thing.objects.filter(domain__name__iexact=domain),
                'title':'Add Thing',
            },
            context_instance=RequestContext(request)
        )

def edit_thing(request,lookup):
    domain, is_created = Domain.objects.get_or_create(name=request.get_host())
    if lookup.isdigit():
        thing = Thing.objects.get(id=lookup,domain=domain)
    else:
        thing = Thing.objects.get(slug=lookup,domain=domain)
    if request.method == 'POST':
        form = ThingForm(request.POST,instance=thing)
        if form.is_valid():
            cd = form.cleaned_data
            obj = form.save(commit=False)
            obj.slug = slugify(cd['name'])
            obj.save()
            return HttpResponseRedirect('/thing/%s' % slugify(cd['name']))
    else:
        form = ThingForm(instance=thing)
        return render_to_response(
            'add_thing.html',
            {
                'form':form,
                'site_name':settings.SITE_NAME,
                'title':'Edit Thing',
                'things': Thing.objects.filter(domain__name__iexact=domain),
            },
            context_instance=RequestContext(request)
        )

def view_thing(request,lookup):
    domain, is_created = Domain.objects.get_or_create(name=request.get_host())
    if lookup.isdigit():
        thing = Thing.objects.get(id=lookup,domain=domain)
    else:
        thing = Thing.objects.get(slug=lookup,domain=domain)
    return render_to_response(
        'view_thing.html',
        {
            'site_name':settings.SITE_NAME,
            'title':'View thing',
            'thing':thing,
            'things': Thing.objects.filter(domain__name__iexact=domain),
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
            'things': Thing.objects.filter(domain__name__iexact=domain),
        },
        context_instance=RequestContext(request)
    )
