from django.shortcuts import (
	render,
	redirect,
	get_object_or_404,
)
from django.core.mail import send_mail

from .forms import (
	PromotionCreationForm,
	EmailForm,
)
from .models import Promotion
from book.models import Book
from users.models import Customer

# Create your views here.
def send_subscribers_email(request):
	template_name = 'promotion/send_email.html'
	context = {}

	print('test')
	# Check if user is logged in and is a staff member.
	if not request.user.is_authenticated or not request.user.is_staff:
		return redirect('bookstore:home')
	# POST request.
	elif request.method == 'POST':
		print('POST')
		# Get the form from the request.
		email_form = EmailForm(
			request.POST,
		)
		# Check if the form is valid.
		if email_form.is_valid():
			# Get data from form.
			subject = email_form.cleaned_data['subject']
			message = email_form.cleaned_data['message']
			# Get all the subscribed customers.
			subscribed_customers = Customer.objects.all().filter(
				subscribed=True,
			)
			# Send the email to everyone.
			for customer in subscribed_customers:
				customer.user.email_user(subject, message)
			# Redirect back to promo_list.
			return redirect('promotion:promo_list')
		# Form is not valid.
		else:
			print('Not valid!')
			# Put form back in context dict.
			context.update({
				'email_form': email_form,
			})
			# Render template with context and form with errors.
			return render(request, template_name, context)
	# GET request.
	else:
		print('GET')
		# Create an EmailForm
		email_form = EmailForm()
		# Put the form in the context dict.
		context.update({
			'email_form': email_form,
		})
		# Render the template with the context.
		return render(request, template_name, context)

def feature_book(request, book_id):
    # Define the template and an empty context dict.
	template_name = ''
	context = {}

	if not request.user.is_authenticated or not request.user.is_staff:
		return redirect('bookstore:home')
	else:
        # Get the Book or 404 because it doesn't exist.
		book = get_object_or_404(Book, id=book_id)
		if book.featured:
			book.featured = False
		else:
			book.featured = True
        # Save the changes.
		book.save()
        # Redirect to the
		return redirect('promotion:books')

def books(request):
	# Define the template and an empty context dict.
	template_name = 'promotion/site_books.html'
	context = {}

	if not request.user.is_authenticated or not request.user.is_staff:
		return redirect('bookstore:home')
	else:
	    # Get all of the Books.
		books = Book.objects.all()

	    # Put all the books in the context dict.
		context.update({
			'books': books,
		})

		# Render the template with the context dict.
		return render(request, template_name, context)

def delete_promo(request, promo_id):
    # Define the template and an empty context dict.
	template_name = ''
	context = {}

	# Check to make sure the request user is logged in and is staff
	if not request.user.is_authenticated or not request.user.is_staff:
		return redirect('bookstore:home')
	else:
		# Get the Promotion from the DB.
		promo = Promotion.objects.get(id=promo_id)
		# Delete the Promotion from the DB.
		promo.delete()
        # Redirect to promotion list.
		return redirect('promotion:promo_list')

def edit_promo(request, promo_id):
    # Define the template and en empty context dict.
	template_name = 'promotion/edit_promo.html'
	context = {}

	# If the user isn't logged in or the user is logged in, but isn't a staff member.
    # Redirect to home page.
	if not request.user.is_authenticated or not request.user.is_staff:
		return redirect('bookstore:home')
	elif request.method == 'POST':
        # Get the Promotion from the DB.
		promo = Promotion.objects.get(id=promo_id)
        # Get the date from the form.
		promo_form = PromotionCreationForm(
			request.POST,
			instance=promo,
		)
        # Check if the form is valid.
		if promo_form.is_valid():
            # Save to DB.
			promo_form.save()
            # Redirect to promotion list page.
			return redirect('promotion:promo_list')
		else:
            # Put the form back in the context dict.
			context.update({
				'promo_form': promo_form,
			})
            # Render the template with the context.
			return render(request, template_name, context)
	else:
        # Get the Promotion from the DB.
		promo = Promotion.objects.get(id=promo_id)
        # Make the Form from the Promotion instance.
		promo_form = PromotionCreationForm(instance=promo)
		context.update({
			'promo_form': promo_form,
		})
    # Render the template with the context dict.
	return render(request, template_name, context)

def add_promo(request):
    # Define the template and an empty context dict.
	template_name = 'promotion/add_promo.html'
	context = {}

    # If the user isn't logged in or the user is logged in, but isn't a staff member.
    # Redirect to home page.
	if not request.user.is_authenticated or not request.user.is_staff:
		return redirect('bookstore:home')
	elif request.method == 'POST':
        # Get the form from the request.
		promo_form = PromotionCreationForm(
			request.POST,
		)
        # Check if the form is valid.
		if promo_form.is_valid():
            # Save the Promotion in the DB.
			promo = promo_form.save()
			return redirect('promotion:promo_list')
        # Form is not valid.
		else:
            # Put the form back in the context dict.
			context.update({
				'promo_form': promo_form,
			})
            # Render the form with the errors.
			return render(request, template_name, context)
	else:
        # Create a PromotionCreationForm to send to user.
		promo_form = PromotionCreationForm()
        # Put the form in the context dict.
		context.update({
			'promo_form': promo_form,
		})
    # Render the template with the context.
	return render(request, template_name, context)

def promo_list(request):
    # Define the template and an empty context dict.
	template_name = 'promotion/promo_list.html'
	context = {}

    # If the user isn't logged in or the user is logged in, but isn't a staff member.
    # Redirect to the home page.
	if not request.user.is_authenticated or not request.user.is_staff:
		return redirect('bookstore:home')
    # User is logged in and is a staff member.
	else:
		promos = Promotion.objects.all()
		context.update({
			'promos': promos,
		})
    # Render the template with the context.
	return render(request, template_name, context)
