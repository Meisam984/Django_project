from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('list/', views.list_cars, name='list'),
    path('add/', views.add_cars, name='add'),
    path('remove/', views.remove_cars, name='remove')
]
