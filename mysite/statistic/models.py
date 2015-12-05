from django.db import models
from django.contrib import admin
# Create your models here.
class Event(models.Model):
    event = models.CharField(max_length=512)
    time = models.DateTimeField()

class Route(models.Model):
    routeid = models.CharField(max_length=64)
    routeip = models.CharField(max_length=32)
    time = models.DateTimeField()

class SnapShot(models.Model):
    linkerid = models.CharField(max_length=32)
    delay = models.IntegerField()
    sendspeed = models.IntegerField()
    recvspeed = models.IntegerField()
    sendflow = models.IntegerField()
    recvflow = models.IntegerField()
    sendpackets = models.IntegerField()
    sevrecv = models.IntegerField()
    recvpackets = models.IntegerField()
    sevsend = models.IntegerField()
    totalsendflow = models.IntegerField()
    totalrecvflow = models.IntegerField()
    totalsendpackets = models.IntegerField()
    totalrecvpackets = models.IntegerField()
    perfspeed = models.FloatField()
    perfjiter = models.FloatField()
    perflr = models.IntegerField()
    time = models.DateTimeField()

class EventAdmin(admin.ModelAdmin):
    list_display = ('event','time')

class RouteAdmin(admin.ModelAdmin):
    list_display = ('routeid', 'time')

class SnapShotAdmin(admin.ModelAdmin):
    list_display = ('linkerid', 'time')

admin.site.register(Event, EventAdmin)
admin.site.register(SnapShot, SnapShotAdmin)
admin.site.register(Route, RouteAdmin)
