from statistic.views import first, archive, archive1, archive2
from django.conf.urls import patterns, url
urlpatterns = patterns('',
    url(r'^event/', archive),
    url(r'^snapshot/', archive1),
    url(r'^route/', archive2),
    url(r'^$', first),
)
