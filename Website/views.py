from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Employee
from .models import Department

# Create your views here.
def index(request):
    return render(request, 'Website/index.html')

def employees(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'Website/employees.html', context)

def departments(request):
    return render(request, 'Website/departments.html')

def computers(request):
    return render(request, 'Website/computers.html')

def training(request):
    return render(request, 'Website/training.html')