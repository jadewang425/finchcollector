from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Finch, Toy

# import the FeedingForm
from .forms import FeedingForm

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
    # create a list of toys this finch does have
    id_list = finch.toys.all().values_list('id')
    # query for toys this finch doesn't have
    toys_doesnt_have = Toy.objects.exclude(id__in=id_list)
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {'finch': finch, 'feeding_form': feeding_form, 'toys': toys_doesnt_have})

class FinchCreate(CreateView):
    model = Finch
    fields = ['breed', 'origin', 'description']

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['origin', 'description']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)

# Toy views
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    def form_valid(self, form):
        return super().form_valid(form)

class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys'

def assoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
    Finch.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)