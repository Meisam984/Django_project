from django.shortcuts import render
from office.models import Patient

# Create your views here.
def list_patients(request):
    all_patients = Patient.objects.all()
    context = {'patients': all_patients}
    
    return render(request, 'office/list.html', context=context)
