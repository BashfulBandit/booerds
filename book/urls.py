from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^$', views.list, name='list'),
    re_path('^(?P<id>(\d+))/$', views.details, name='details'),
    re_path('^add_book/(?P<vendor_id>(\d+))/$', views.add_book, name='add_book'),
    re_path('^delete_book/(?P<book_id>(\d+))/$', views.delete_book, name='delete_book'),
    re_path('^edit_book/(?P<book_id>(\d+))/$', views.edit_book, name='edit_book'),
]
