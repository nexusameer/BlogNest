from django.shortcuts import render
from app.models import *
from django.views.generic import TemplateView
from app.mixins import *
# Create your views here.

class HomeView(CommonContextMixin, TemplateView):
    template_name = 'home.html'
