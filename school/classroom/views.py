from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.forms import ContactForm
from classroom.models import Teacher

# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    model = Teacher
    #model_form.html
    #.save()
    fields = '__all__'
    success_url = reverse_lazy('classroom:thank_you')

class TeacherListView(ListView):
    model = Teacher
    # model_list.html
    context_object_name = 'teacher_list'
    queryset = Teacher.objects.order_by('first_name')

class TeacherDetailView(DetailView):
    model = Teacher
    #model_detail.html
    # PK --> {{teacher}}

class TeacherUpdateView(UpdateView):
    model = Teacher
    #Shares model_form.html
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')
    # PK --> {{teacher}}
    
class TeacherDeleteView(DeleteView):
    model = Teacher
    #model_confirm_delete.html
    success_url = reverse_lazy('classroom:list_teacher')
    # PK --> {{teacher}}

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    #Success URL
    success_url = reverse_lazy('classroom:thank_you')
    #What to do with form
    def form_valid(self, form) -> HttpResponse:
        print(form.cleaned_data)
        return super().form_valid(form)

    