from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^$', views.promo_list, name='promo_list'),
	re_path('^add/$', views.add_promo, name='add_promo'),
	re_path('^delete/(?P<promo_id>(\d+))/$', views.delete_promo, name='delete_promo'),
	re_path('^edit/(?P<promo_id>(\d+))/$', views.edit_promo, name='edit_promo'),
	re_path('^books/$', views.books, name='books'),
	re_path('^books/feature_book/(?P<book_id>(\d+))/$', views.feature_book, name='feature_book'),
    re_path('^email/$', views.send_subscribers_email, name='send_subscribers_email'),
]
