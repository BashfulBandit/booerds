from django.urls import re_path, include

urlpatterns = [
    # /
    re_path('', include(('shop.urls', 'shop'), namespace='shop')),
]
