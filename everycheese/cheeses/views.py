from re import A
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView 

from .models import Cheese

class CheeseListView(ListView):
    model = Cheese

class CheeseDetails(DetailView):
    model = Cheese

class CheeseCreateView(LoginRequiredMixin, CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness', 'country',]
