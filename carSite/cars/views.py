from django.shortcuts import render

# Create your views here.
def list_cars(request):
    return render(request, 'cars/list.html')

def add_cars(request):
    return render(request, 'cars/add.html')

def remove_cars(request):
    return render(request, 'cars/remove.html')