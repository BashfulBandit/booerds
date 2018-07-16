from django.urls import (
    re_path,
)
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    re_path('^$', views.user_login, name='user_login'),
	# re_path('^password_reset/$', auth_views.password_reset, name='password_reset'),
	# re_path('^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
	# re_path('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
	# re_path('^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    re_path('^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    re_path('^account_activation_sent/$', views.account_activation_sent, name='account_activation_sent'),
    re_path('^(?P<id>(\d+))/$', views.profile, name='profile'),
    re_path('^logout/$', views.user_logout, name='user_logout'),
    re_path('^register/$', views.customer_register, name='customer_register'),
    re_path('^register/vendor/$', views.vendor_register, name='vendor_register'),
]
