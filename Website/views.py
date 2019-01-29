from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from datetime import datetime

from .models import Training_Program

# Create your views here.
def index(request):
    return render(request, 'Website/index.html')

def employees(request):
    return render(request, 'Website/employees.html')

def departments(request):
    return render(request, 'Website/departments.html')

def computers(request):
    return render(request, 'Website/computers.html')

def training(request):
  ''' Get all of the training programs from DB,
  sort by most recent date,
  filter out programs occurring before today's date,
  and send to training.html '''

  training_list = Training_Program.objects.all().order_by('start_date').filter(start_date__gt=datetime.today())

  context = {'training_list': training_list}

  return render(request, 'Website/training.html', context)