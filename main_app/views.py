from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch

# data for testing purpose
# finches = [
#   {'breed': 'American Goldfinch', 'description': 'Breeding males are bright yellow with black forehead, black wings with white markings', 'origin': 'North America'},
#   {'breed': 'Eurasian Bullfinch', 'description': 'The Eurasian bullfinch is a bulky bull-headed bird. The upper parts are grey; the flight feathers and short thick bill are black', 'origin': "Europe and Asia"},
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', {'finch': finch})

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['origin', 'description']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'