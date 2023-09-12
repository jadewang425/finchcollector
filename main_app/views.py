from django.shortcuts import render

# data for testing purpose
finches = [
  {'breed': 'American Goldfinch', 'description': 'Breeding males are bright yellow with black forehead, black wings with white markings', 'origin': 'North America'},
  {'breed': 'Eurasian Bullfinch', 'description': 'The Eurasian bullfinch is a bulky bull-headed bird. The upper parts are grey; the flight feathers and short thick bill are black', 'origin': "Europe and Asia"},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches})