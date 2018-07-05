from django.urls import re_path

from . import views

urlpatterns = [
    # /u/
    re_path('^$', views.index, name='index'),
    # /u/login/
    re_path('^login/$', views.user_login, name='login'),
    # /u/logout/
    re_path('^logout/$', views.user_logout, name='logout'),
    # /u/register/
    re_path('^register/$', views.user_register, name='register'),
    # /u/<user_id>/
    re_path('^(\d+)/$', views.user_profile, name='profile'),
]
