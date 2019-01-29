from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Department, Employee, Computer, Training_Program


# Create your views here.
def index(request):      
    return render(request, 'Website/index.html')

def employees(request):
    return render(request, 'Website/employees.html')    

def departments(request):
    return render(request, 'Website/departments.html')        

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
    return render(request, 'Website/training.html')