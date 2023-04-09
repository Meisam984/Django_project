from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from catalog.models import Book, BookInstance
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_available_instances = BookInstance.objects.filter(status__exact='a').count()

    context = {
                'num_books': num_books,
                'num_inst': num_instances,
                'num_avail_inst': num_available_instances
              }
    
    return render(request, 'catalog/index.html', context=context)


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = "__all__"

class BookDetail(DetailView):
    model = Book

@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'catalog/signup.html'
    success_url = reverse_lazy('login')

class CheckedOutBooksByUser(LoginRequiredMixin, ListView):
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5
    
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)
    
    def get_context_data(self):
        context = {'user': self.request.user}
        return context


