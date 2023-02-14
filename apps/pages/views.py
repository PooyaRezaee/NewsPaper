from django.shortcuts import render
from django.views.generic import TemplateView

__all__ = [
    'HomePageView',
]

class HomePageView(TemplateView):
    template_name = 'home.html'