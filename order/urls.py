from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^(?P<payment_method>(\w+))/$', views.place_order, name='place_order'),
    re_path('^details/(?P<id>(\d+))/$', views.order_details, name='order_details'),
]
