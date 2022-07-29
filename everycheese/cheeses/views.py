from django.views.generic import ListView, DetailView, CreateView

from .models import Cheese

class CheeseListView(ListView):
    model = Cheese

class CheeseDetails(DetailView):
    model = Cheese

class CheeseCreateView(CreateView):
    model = Cheese
    fields = ['name', 'description', 'firmness', 'country',]
