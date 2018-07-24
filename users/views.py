from django.shortcuts import (
	render,
	redirect,
	get_object_or_404,
)
from django.contrib.auth.models import User
# For Token Generating on Registration and Password Reset.
from django.utils.encoding import (
	force_bytes,
	force_text,
)
from django.utils.http import (
	urlsafe_base64_encode,
	urlsafe_base64_decode,
)
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
# For authenticating Django User.
from django.contrib.auth import (
	authenticate,
	login,
	logout,
)
# Default Django User Authentication Form used to login.
from django.contrib.auth.forms import AuthenticationForm

# Importing our models and forms.
from book.models import Book
from order.models import Order
from .tokens import account_activation_token
from .models import (
	Customer,
	Vendor,
)
from .forms import (
	MyUserCreationForm,
	CustomerCreationForm,
	VendorCreationForm,
	CustomerChangeForm,
	VendorChangeForm,
)

def deactivate(request, id):
	template_name = ''
	context = {}

	print(request.user.id)
	print(id)
	if not request.user.is_authenticated or not str(request.user.id) == id:
		print('home')
		return redirect('bookstore:home')
	else:
		print("here")
		user = get_object_or_404(
			User,
			id=id,
		)
		user.is_active = False
		user.save()
		return redirect('bookstore:home')

def user_login(request):
    # Define the template and the empty context dict.
	template_name = 'users/login.html'
	context = {}

    # If the user if already logged in, then redirect to profile page.
	if request.user.is_authenticated:
		return redirect('users:profile', id=request.user.id)
    # If the request is a POST.
	elif request.method == 'POST':
        # Get the form from the request.
		form = AuthenticationForm(data=request.POST)
        # Check if the form is valid.
		if form.is_valid():
            # Get the data from the form.
			username = form.cleaned_data['username']
			raw_password = form.cleaned_data['password']
            # authenticate the user.
			user = authenticate(
				request,
				username=username,
				password=raw_password
			)
			if user is not None:
				# Log the user in.
				login(request, user)
				# Send them to the page based on the URL.
				if 'next' in request.GET:
					return redirect(request.GET['next'])
				else:
					return redirect('users:profile', id=user.id)
        # If the form isn't valid then send them the form back with errors.
		else:
			context.update({
				'form': form,
			})
			return render(request, template_name, context)
    # GET request.
	else:
        # Generate a default form.
		form = AuthenticationForm()
		context.update({
			'form': form,
		})
	    # Render the template with the context dict.
		return render(request, template_name, context)

def user_logout(request):
    # If they tried to logout via a link in the page get the 'next' variable.
	if request.method == 'GET' and 'next' in request.GET:
		next = request.GET['next']
	else:
		next = 'bookstore:home'
    # Log them out.
	logout(request)
    # Send them to the page they were on or the home page.
	return redirect(next)

def profile(request, id):
    # Define the template and the context dict.
	template_name = 'users/profile.html'
	context = {}

    # If the user is not logged in, then redirect them to login.
	if not request.user.is_authenticated:
		return redirect('bookstore:home')
    # Make sure the request.user is the same as the user requested.
	elif str(request.user.id) == id:
        # Get the User from the DB.
		user = get_object_or_404(User, id=id)
        # Get the user profile.
		profile = None
		books = None
		orders = None
		if hasattr(user, 'customer'):
			profile = user.customer
			orders = Order.objects.all().filter(customer=request.user.customer)
		elif hasattr(user, 'vendor'):
			profile = user.vendor
			books = Book.objects.all().filter(vendor=request.user.vendor)
        # Put the data in the context dict.
		context.update({
			'user': user,
			'profile': profile,
			'books': books,
			'orders': orders,
		})
        # Render the template with the context dict.
		return render(request, template_name, context)
    # The request is for a page they don't has access to.
	else:
        # Redirect to home page.
		return redirect('bookstore:home')

def edit_profile(request, id):
    # Define the template and the empty context dict.
	template_name = 'users/edit_profile.html'
	context = {}

    # If the user is not logged in, then redirect them to the login.
	if not request.user.is_authenticated:
		return redirect('users:user_login')
    # request is a POST.
	elif request.method == 'POST':
        # Check to figure out if user is customer or vendor and get their profile form.
		if hasattr(request.user, 'customer'):
			form = CustomerChangeForm(
				request.POST,
				request.FILES,
				instance=request.user.customer,
			)
		elif hasattr(request.user, 'vendor'):
			form = VendorChangeForm(
				request.POST,
				request.FILES,
				instance=request.user.vendor,
			)

        # Check if the form is valid.
		if form.is_valid():
            # Save the form.
			profile = form.save()
            # Save the profile.
			profile.save()
            # Redirect back to profile page.
			return redirect('users:profile', id=request.user.id)
        # Form is invalid. Return them the form with errors.
		else:
			context.update({
				'form', form,
			})
			return render(request, template_name, context)
    # GET request.
	else:
        # Check to figure out if user is customer or vendor.
		if hasattr(request.user, 'customer'):
			form = CustomerChangeForm(
				instance=request.user.customer,
			)
		elif hasattr(request.user, 'vendor'):
			form = VendorChangeForm(
				instance=request.user.vendor,
			)

        # Put form in context dict.
		context.update({
			'form': form,
		})

        # Render the template with the context dict.
		return render(request, template_name, context)

def account_activation_sent(request):
    # Define template and empty context dict.
	template_name = 'users/account_activation_sent.html'
	context = {}
	return render(request, template_name, context)

def unsubscribe(request):
    # Define template and empty context dict.
	template_name = ''
	context = {}

    # If user is not logged in then redirect to login page.
	if not request.user.is_authenticated:
		return redirect('users:user_login')
    # User is logged in.
	else:
        # Get customer object from DB.
		customer = Customer.objects.get(user=request.user)
        # Change subscribed value.
		if customer.subscribed:
			customer.subscribed = False
		else:
			customer.subscribed = True
        # Save changes.
		customer.save()
        # Redirect them back to their profile page.
		return redirect('users:profile', id=request.user.id)

def activate(request, uidb64, token):
    # Define the template and an empty context dict.
	template_name = 'users/account_activation_invalid.html'
	context = {}

    # Try statement to get the user id from the uidb64 parameter.
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

    # If user exists and the token is valid.
	if user is not None and account_activation_token.check_token(user, token):
        # Activate User, save the change, and log them in.
		user.is_active = True
		user.save()
		login(request, user)
        # Redirect to profile page.
		return redirect('users:profile', id=user.id)
    # If user doesn't exists or token is invalid send them to invalid page.
	else:
		return render(request, template_name, context)

def customer_register(request):
    # Define the template and the empty context dict.
	template_name = 'users/customer_register.html'
	context = {}

    # If user is already logged in, then redirect to profile page.
	if request.user.is_authenticated:
		return redirect('users:profile', id=request.user.id)
    # If POST, get form data and validate it.
	elif request.method == 'POST':
        # Get the forms from the request.
		user_form = MyUserCreationForm(request.POST)
		customer_form = CustomerCreationForm(request.POST, request.FILES)

        # Make sure the forms are valid.
		if user_form.is_valid() and customer_form.is_valid():
            # Make a user from the user_form.
			user = user_form.save()
			customer = customer_form.save()
            # Set user.is_active to False.
			user.is_active = False
			customer.user = user
			user.save()
			customer.save()
            # Gather information to email the user.
			current_site = get_current_site(request)
			subject = 'Activate Your boo(kn)erds Account'
			message = render_to_string('users/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),
			})
            # Email the user.
			user.email_user(subject, message)
			customer_form.save()
            # Redirect to account_activation_sent.
			return redirect('users:account_activation_sent')
        # If form data isn't valid, then get the forms to send back to user.
		else:
			context.update({
				'user_form': user_form,
				'customer_form': customer_form,
			})
			return render(request, template_name, context)
    # GET request.
	else:
        # Make default forms.
		user_form = MyUserCreationForm()
		customer_form = CustomerCreationForm()

        # Put forms in context dict.
		context.update({
			'user_form': user_form,
			'customer_form': customer_form,
		})
	    # Render the template with the context dict.
		return render(request, template_name, context)

def vendor_register(request):
    # Define the template and the empty context dict.
	template_name = 'users/vendor_register.html'
	context = {}

    # If user is already logged in, redirect to profile page.
	if request.user.is_authenticated:
		return redirect('users:profile', id=request.user.id)
    # If POST, get form data and validate.
	elif request.method == 'POST':
        # Get the forms from the request.
		user_form = MyUserCreationForm(request.POST)
		vendor_form = VendorCreationForm(request.POST, request.FILES)

        # Check if valid, if not return the form to the user to fix.
		if user_form.is_valid() and vendor_form.is_valid():
            # Save the user_form
			user = user_form.save()
			vendor = vendor_form.save()
            # Set user.is_active to False, so we can e-mail verify.
			user.is_active = False
			vendor.user = user
			user.save()
			vendor.save()
            # Gather information to email to the user.
			current_site = get_current_site(request)
			subject = 'Activate Your boo(kn)erds Account'
			message = render_to_string('users/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),
			})
            # Email the user.
			user.email_user(subject, message)
            # Redirect to account_activation_sent
			return redirect('users:account_activation_sent')
        # Invalid form(s), return the forms to the user.
		else:
			context.update({
				'user_form': user_form,
				'vendor_form': vendor_form,
			})
			return render(request, template_name, context)
    # GET request.
	else:
        # Create default forms.
		user_form = MyUserCreationForm()
		vendor_form = VendorCreationForm()

        # Put the forms in the context dict.
		context.update({
			'user_form': user_form,
			'vendor_form': vendor_form,
		})
	    # Render the template with the context.
		return render(request, template_name, context)
