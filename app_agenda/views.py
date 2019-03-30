from django.shortcuts import render
from django.views.generic import ListView

from .models import AgendaInstitucional


class HomePageView(ListView):
    model = AgendaInstitucional
    template_name = 'app_agenda/home.html'