from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^books/$', views.list, name='list'),
    re_path('^books/(?P<id>(\d+))/$', views.details, name='details'),
    re_path('^$', views.home, name='home'),
]
