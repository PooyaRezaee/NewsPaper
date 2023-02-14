from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SingUpForm

__all__ = [
    'SignUpView'
]

class SignUpView(CreateView):
    form_class = SingUpForm 
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
