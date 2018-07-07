from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False)
    name = models.CharField(max_length=254, blank=False)
    # date_of_birth = models.DateField(blank=False)
    # address = models.CharField(max_length=254, blank=False)
    # zipcode = models.CharField(max_length=20, blank=False)
    # city = models.CharField(max_length=50, blank=False)
    # state = models.CharField(max_length=50, blank=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
        # 'date_of_birth'
        # 'address',
        # 'zipcode',
        # 'city',
        # 'state',
    ]
