# Define Django things here.
from django.shortcuts import (
    render,
)
from random import randint
from book.models import Book
from promotion.models import Promotion

# Create your views here.
def home(request):
	# Define the template and an empty context dict.
	template_name = 'bookstore/home.html'
	context = {}

	promo = None
	# Find out how many Promotions are for the frontpage.
	num_frontpage_promos = Promotion.objects.all().filter(frontpage=True).count()
	if num_frontpage_promos > 0:
		# Get a random number between 0 and the number of frontpage promotions.
		random_index = randint(0, num_frontpage_promos - 1)
		# Get a single Promotion from the frontpage promotions.
		promo = Promotion.objects.all().filter(frontpage=True)[random_index]

	# Get some books
	featured_books = Book.objects.all().filter(featured=True)

	# Add the books the context dict.
	context.update({
		'featured_books': featured_books,
		'promo': promo,
	})

	# Render the reponse.
	return render(request, template_name, context)
