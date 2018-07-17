from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^(?P<id>(\d+))/$', views.add_to_cart, name='add_to_cart'),
    re_path('^show_cart/$', views.show_cart, name='show_cart')
    #re_path('^checkout',views.checkout, name = 'checkout')
]
