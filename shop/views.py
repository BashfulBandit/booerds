from django.shortcuts import (
	render,
	redirect
)

def home(request):
	context = {
		# This would get all the Books
		# This would get the active Promotion
	}
	return render(request, 'shop/home.html', context)
