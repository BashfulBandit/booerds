from django.urls import (
    re_path,
)

from . import views

urlpatterns = [
    re_path('^$', views.user_login, name='user_login'),
    re_path('^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    re_path('^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    re_path('^(?P<id>(\d+))/$', views.profile, name='profile'),
    re_path('^(?P<id>(\d+))/edit_profile/$', views.edit_profile, name='edit_profile'),
    re_path('^unsubscribe/$', views.unsubscribe, name='unsubscribe'),
    re_path('^logout/$', views.user_logout, name='user_logout'),
    re_path('^register/$', views.customer_register, name='customer_register'),
    re_path('^register/vendor/$', views.vendor_register, name='vendor_register'),
]
