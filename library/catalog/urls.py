from django.urls import path
from catalog import views

# app_name = 'catalog'

urlpatterns = [
    path('', views.index, name='index'),
    path('book_create/', views.BookCreate.as_view(), name='book_create'),
    path('book_detail/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),
    path('my_view/', views.my_view, name='my_view'),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('profile/', views.CheckedOutBooksByUser.as_view(), name='profile')
]


