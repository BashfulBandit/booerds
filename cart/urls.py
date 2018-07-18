from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^show_cart/$',views.show_cart, name = 'show_cart'),
    re_path('^(?P<id>(\d+))/$', views.cart, name='cart'),
    #re_path('^(?P<id>(\d+))/$', views.delete, name='delete'),
    #re_path('^checkout',views.checkout, name = 'checkout')
    
]
