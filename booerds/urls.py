from django.urls import re_path, include

urlpatterns = [
    # /u/
    re_path('u/', include('users.urls')),
    # /
    re_path('', include('shop.urls')),
]
