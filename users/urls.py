from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^login/$', views.user_login, name='user_login'),
    re_path('^logout/$', views.user_logout, name='user_logout'),
    re_path()
    re_path('^$', views.login, name='login'),
]
