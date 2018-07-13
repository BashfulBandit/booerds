from django.urls import (
    re_path,
)

from . import views

urlpatterns = [
    re_path('^$', views.user_login, name='user_login'),
    re_path('^(?P<id>(\d+))/$', views.profile, name='profile'),
    re_path('^logout/$', views.user_logout, name='user_logout'),
    re_path('^register/$', views.customer_register, name='customer_register'),
    re_path('^register/vendor/$', views.vendor_register, name='vendor_register'),
]
