from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^$', views.show_cart, name='show_cart'),
    re_path('^add/(?P<id>(\d+))/$', views.add_to_cart, name='add_to_cart'),
    re_path('^delete/(?P<id>(\d+))/$', views.delete_from_cart, name='delete_from_cart'),
    #re_path('^checkout/$', views.checkout, name='checkout')
]
