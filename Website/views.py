from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Employee
from .models import Department
from datetime import datetime

from .models import Training_Program

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
    ''' Gets all of the training programs from DB, sorts by most recent date,
    and filters out training programs occurring before current date '''
    training_list = Training_Program.objects.all().order_by('start_date').filter(start_date__gt=datetime.today())
    context = {'training_list': training_list}
    return render(request, 'Website/training.html', context)

def add_training_form(request):
    ''' Directs user to the add training program form '''
    return render(request, 'Website/add_training.html')

def post_training(request):
    ''' Creates new Training Program record in database and redirects to Training page '''
    program = request.POST["program_name"]
    description = request.POST["program_desc"]
    start = request.POST["start_date"]
    end = request.POST["end_date"]
    attendees = request.POST["max_attendees"]
    new_program = Training_Program(program_name=program, program_desc=description, start_date=start, end_date=end, max_attendees=attendees)
    new_program.save()
    return HttpResponseRedirect(reverse('Website:training'))