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
from .tokens import account_activation_token
from .models import (
	Customer,
	Vendor,
)
from .forms import (
	MyUserCreationForm,
	CustomerCreationForm,
	VendorCreationForm,
)

def user_login(request):
	template_name = 'users/login.html'
	context = {}

	if request.user.is_authenticated:
		return redirect('users:profile', id=request.user.id)
	elif request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			raw_password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=raw_password)
			if user is not None:
				login(request, user)
				return redirect('users:profile', id=user.id)
	else:
		form = AuthenticationForm()
		context.update({
			'form': form,
		})
		return render(request, template_name, context)

def user_logout(request):
	if request.method == 'GET' and 'next' in request.GET:
		next = request.GET['next']
	else:
		next = 'bookstore:home'
	logout(request)
	return redirect(next)

def profile(request, id):
	template_name = 'users/profile.html'
	context = {}

	if not request.user.is_authenticated:
		return redirect('bookstore:home')
	if str(request.user.id) == id:
		user = get_object_or_404(User, id=id)
		profile = None
		if hasattr(user, 'customer'):
			profile = user.customer
		elif hasattr(user, 'vendor'):
			profile = user.vendor
		context.update({
			'user': user,
			'profile': profile,
		})
		return render(request, template_name, context)
	# TODO Need to come up with a place to send the user when they request a profile
	# page that isn't their own.
	return render(request, template_name, context)


def account_activation_sent(request):
	template_name = 'users/account_activation_sent.html'
	context = {}
	return render(request, template_name, context)

def activate(request, uidb64, token):
	template_name = 'users/account_activation_invalid.html'
	context = {}

	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return redirect('users:profile', id=user.id)
	else:
		return render(request, template_name, context)

def customer_register(request):
	template_name = 'users/customer_register.html'
	context = {}

	if request.user.is_authenticated:
		return redirect('users:profile', id=request.user.id)
	elif request.method == 'POST':
		user_form = MyUserCreationForm(request.POST)
		customer_form = CustomerCreationForm(request.POST)

		if user_form.is_valid() and customer_form.is_valid():
			user = user_form.save()
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			subject = 'Activate Your boo(kn)erds Account'
			message = render_to_string('users/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),
			})
			user.email_user(subject, message)
			street_address = customer_form.cleaned_data['street_address']
			zipcode = customer_form.cleaned_data['zipcode']
			city = customer_form.cleaned_data['city']
			state = customer_form.cleaned_data['state']
			date_of_birth = customer_form.cleaned_data['date_of_birth']
			customer = Customer.objects.create(
				user=user,
				street_address=street_address,
				zipcode=zipcode,
				city=city,
				state=state,
				date_of_birth=date_of_birth,
			)
			return redirect('users:account_activation_sent')
		# else:
		# 	return redirect('users:customer_register')
	else:
		user_form = MyUserCreationForm()
		customer_form = CustomerCreationForm()

		context.update({
			'user_form': user_form,
			'form': customer_form,
		})
	return render(request, template_name, context)

def vendor_register(request):
	template_name = 'users/vendor_register.html'
	context = {}

	if request.user.is_authenticated:
		return redirect('users:profile', id=request.user.id)
	elif request.method == 'POST':
		user_form = MyUserCreationForm(request.POST)
		vendor_form = VendorCreationForm(request.POST)

		if user_form.is_valid() and vendor_form.is_valid():
			user = user_form.save()
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			subject = 'Activate Your boo(kn)erds Account'
			message = render_to_string('users/account_activation_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token': account_activation_token.make_token(user),
			})
			user.email_user(subject, message)
			street_address = vendor_form.cleaned_data['street_address']
			zipcode = vendor_form.cleaned_data['zipcode']
			city = vendor_form.cleaned_data['city']
			state = vendor_form.cleaned_data['state']
			vendor = Vendor.objects.create(
				user=user,
				street_address=street_address,
				zipcode=zipcode,
				city=city,
				state=state,
			)
			return redirect('users:account_activation_sent')
	else:
		user_form = MyUserCreationForm()
		vendor_form = VendorCreationForm()

		context.update({
			'form_name': 'Vendor Registration Form',
			'user_form': user_form,
			'form': vendor_form,
			'form_button': 'Register',
		})
	return render(request, template_name, context)
