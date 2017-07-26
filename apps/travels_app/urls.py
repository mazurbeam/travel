from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^add$', views.add),
    url(r'^addTrip$', views.addTrip),
    url(r'^destination/(?P<id>\d+)', views.destination),
    url(r'^join/(?P<id>\d+)', views.join)
]
