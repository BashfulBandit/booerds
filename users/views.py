from django.shortcuts import (
	render,
	redirect,
)
from django.contrib.auth import (
	authenticate,
	login,
	logout,
)
from django.contrib.auth.forms import AuthenticationForm

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
	template_name = 'users/forms.html'
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
			'form_name': 'Login',
			'form': form,
		})
		return render(request, template_name, context)

def user_logout(request):
	logout(request)
	return redirect('bookstore:home')

def profile(request, id):
	template_name = 'users/profile.html'
	context = {}

	return render(request, template_name, context)

def customer_register(request):
	template_name = 'users/forms.html'
	context = {}

	if request.user.is_authenticated:
		return redirect('users:profile', id=user.id)
	if request.method == 'POST':
		user_form = MyUserCreationForm(request.POST)
		customer_form = CustomerCreationForm(request.POST)

		if user_form.is_valid() and customer_form.is_valid():
			user_form.save()
			username = user_form.cleaned_data['username']
			raw_password = user_form.cleaned_data['password1']
			user = authenticate(request, username=username, password=raw_password)
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
            # TODO Need to redirect to profile page once profile view is written.
			return redirect('users:profile', id=user.id)
	else:
		user_form = MyUserCreationForm()
		customer_form = CustomerCreationForm()

		context.update({
			'form_name': 'Customer Registration Form',
			'user_form': user_form,
			'form': customer_form,
		})
		return render(request, template_name, context)

def vendor_register(request):
	template_name = 'users/forms.html'
	context = {}

	# TODO Need to turn this on and redirect to profile page.
	# if request.user.is_authenticated:
	# 	return redirect('/')
	if request.method == 'POST':
		user_form = MyUserCreationForm(request.POST)
		vendor_form = VendorCreationForm(request.POST)

		if user_form.is_valid() and vendor_form.is_valid():
			user_form.save()
			username = user_form.cleaned_data['username']
			raw_password = user_form.cleaned_data['password1']
			user = authenticate(request, username=username, password=raw_password)
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
            # TODO Need to redirect to profile page once profile view is written.
			return redirect('/')
	else:
		user_form = MyUserCreationForm()
		vendor_form = VendorCreationForm()

		context.update({
			'form_name': 'Vendor Registration Form',
			'user_form': user_form,
			'form': vendor_form,
		})
		return render(request, template_name, context)
