from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^login/$', views.user_login, name='user_login'),
    re_path('^logout/$', views.user_logout, name='user_logout'),
    re_path('^register/$', views.register, name='register'),
    re_path('^register/customer/$', views.customer_register, name='customer_register'),
    re_path('^register/vendor/$', views.vendor_register, name='vendor_register'),
    re_path('^profile/$', views.profile, name='profile'),
    re_path('^profile/(?P<id>(\d+))/$', views.profile, name='profile'),
    re_path('^books/$', views.list, name='list'),
    re_path('^books/(?P<id>(\d+))/$', views.details, name='details'),
    re_path('^$', views.home, name='home'),
]
