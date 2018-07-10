from django.urls import re_path, include
from django.contrib import admin

urlpatterns = [
    # /admin/
    re_path('admin/', admin.site.urls),
    # /
    re_path('', include(('shop.urls', 'shop'), namespace='shop')),
]
