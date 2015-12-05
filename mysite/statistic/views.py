from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from statistic.models import Event, SnapShot, Route
def first(request):
    t = loader.get_template("index.html")
    c = Context()
    return HttpResponse(t.render(c))

def archive(request):
    events = Event.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'events' : events})
    return HttpResponse(t.render(c))

def archive1(request):
    snapshots = SnapShot.objects.all().order_by('-id')
    t = loader.get_template("snapshot.html")
    c = Context({'snapshots' : snapshots})
    return HttpResponse(t.render(c))

def archive2(request):
    routes = Route.objects.all()
    t = loader.get_template("route.html")
    c = Context({'routes' : routes})
    return HttpResponse(t.render(c))
