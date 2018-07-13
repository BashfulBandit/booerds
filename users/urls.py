from django.urls import (
    include,
    re_path,
)

from .views import (
    customer,
    vendor,
)

urlpatterns = [
    re_path('^$', include('django.contrib.auth.urls')),
    re_path('^register/$', customer.CustomerRegisterView.as_view(), name='customer_register'),
    re_path('^register/customer/$', customer.CustomerRegisterView.as_view(), name='customer_register'),
    re_path('^register/vendor/$', vendor.VendorRegisterView.as_view(), name='customer_register'),
]
