from django.shortcuts import render, redirect
from django.urls import reverse
from . import models

# Create your views here.
def list_cars(request):
    all_cars = models.Car.objects.all()
    all_cars_dict = {'all_cars': all_cars}

    return render(request, 'cars/list.html', context=all_cars_dict)

def add_cars(request):
    if request.POST:
        brand = request.POST['brand']
        year = request.POST['year']
        models.Car.objects.create(brand=brand, year=year)
        return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/add.html')

def remove_cars(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print("pk not found")
            return redirect(reverse('cars:list'))
    else:
        return render(request, 'cars/remove.html')