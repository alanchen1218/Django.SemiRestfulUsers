from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^first_app/new$', views.new),   # This line has changed! Notice that urlpatterns is a list, the comma is in
    url(r'^first_app/create$', views.create),
    url(r'^first_app/(?P<number>\d+)/edit$', views.edit),
    url(r'^first_app/(?P<number>\d+)$', views.show),
    url(r'^first_app/(?P<number>\d+)/destroy$', views.destroy),
    url(r'^first_app/userupdate$', views.update),

]  