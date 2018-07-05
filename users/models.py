from django.db import models
from django.contrib.auth.models import AbstractUser

##################################################################################################
## Below is a list of functions inherited from the AbstractBaseUser                             ##
## get_full_name():                                                                             ##
## get_short_name():                                                                            ##
## get_username(): return self.USERNAME_FIELD                                                   ##
## classmethod clean(): normalizes the username by calling normalize_username()                 ##
## classmethod get_email_field_name(): return self.EMAIL_FIELD                                  ##
## is_authenticated: Attribute to say whether the user is logged in.                            ##
## is_anonymous: Attribute given to Users who aren't logged in.                                 ##
## set_password(raw_password): Hashes password and sets User Password to it.                    ##
## check_password(raw_password): Returns True is the raw_password matches stored hash password. ##
## set_unusable_password(): Marks user as having no password set.                               ##
## has_usable_password(): Returns False if set_unusable_password has been called.               ##
## get_session_auth_hash(): returns HMAC of the password field.                                 ##
##################################################################################################
class User(AbstractUser):
    USER_TYPES = [
        ('C', 'Customer'),
        ('P', 'Publisher'),
        ('V', 'Vendor'),
    ]
    name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=254, unique=True, blank=False)
    user_type = models.CharField(max_length=1, choices=USER_TYPES, default='C')
    date_of_birth = models.DateTimeField(blank=False)
    address = models.CharField(max_length=254, blank=False)
    zipcode = models.CharField(max_length=20, blank=False)
    city = models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
        'user_type',
        'date_of_birth'
        'address',
        'zipcode',
        'city',
        'state',
    ]
# Forms you can use with this Custom User Model
# AuthenticationForm: Uses the username field specified by USERNAME_FIELD
# SetPasswordForm
# PasswordChangeForm
# AdminPasswordChangeForm
#
# PasswordReserForm: Assumes that the Custom User Model that stores the user's email
#   address with the name returned by get_email_field_name() that can be used to identify
#   the user and a boolean field named is_active to prevent password resets for inactive
#   users.
#
# The following Forms need to be rewritten
# UserCreationForm
# UserChangeForm
