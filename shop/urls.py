from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
	re_path('^u/login/$', views.login, name='login'),
	re_path('^u/register/$', views.register, name='register'),
	re_path('^u/logout/$', views.logout, name='logout'),
	re_path('^u/(\d+)/$', views.profile, name='profile'),
]
