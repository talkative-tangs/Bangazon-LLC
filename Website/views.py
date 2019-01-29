from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Employee
from datetime import datetime
from .models import Training_Program, Department, Employee, Computer

# Create your views here.
def index(request):
    return render(request, 'Website/index.html')

def employees(request):
    employees = Employee.objects.order_by('last_name')
    context = {'employees': employees}
    return render(request, 'Website/employees.html', context)

def departments(request):
    '''Lists all departments sorted by name'''
    department_list = Department.objects.all().order_by('department_name')
    context = { 'department_list': department_list }
    return render(request, 'Website/departments.html', context)

def computers(request):
    """Show a list of all computers"""
    computers = Computer.objects.order_by('manufacturer')
    context = {
        'computers': computers,
    }

    return render(request, 'Website/computers.html', context)

def computer(request, computer_id):
    """Show a single computer and its details"""
    computer = Computer.objects.get(id=computer_id)
    context = {
        'computer': computer,
        }

    return render(request, 'Website/computer.html', context)

def new_computer(request):
    """view for adding new computers"""
    if request.method != 'POST':
        return render(request, 'Website/new_computer.html')
    else:
        manufacturer = request.POST['manufacturer']
        model = request.POST['model']
        purchase_date = request.POST['purchase_date']

        new_computer = Computer(
            manufacturer=manufacturer,
            model=model,
            purchase_date=purchase_date,
            )
        new_computer.save()
        return HttpResponseRedirect(reverse('Website:computers'))


def training(request):
    ''' Gets all of the training programs from DB, sorts by most recent date,
    and filters out training programs occurring before current date '''
    training_list = Training_Program.objects.all().order_by('start_date').filter(start_date__gte=datetime.today())
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