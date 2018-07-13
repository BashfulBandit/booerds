from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import CustomerRegisterForm
from ..models import User

class CustomerRegisterView(CreateView):
    model = User
    form_class = CustomerRegisterForm
    template_name = 'accounts/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        loggin(self.request, user)
        return redirect('/')
