from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
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
class MyUser(AbstractUser):
	username = None
	email = models.EmailField(unique=True, blank=False)
	full_name = models.CharField(max_length=254, blank=False)

	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = [
		'full_name',
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
