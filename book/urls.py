from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^$', views.list, name='list'),
    re_path('^(?P<id>(\d+))/$', views.details, name='details'),
]
