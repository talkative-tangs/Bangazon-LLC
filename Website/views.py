from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
# from django.db.models import Q
from datetime import datetime
from .models import Training_Program, Department, Employee, Computer, Join_Computer_Employee, Join_Training_Employee

# Create your views here.
def index(request):
    return render(request, 'Website/index.html')

def employees(request):
    '''Lists all Bangazon employees in ascending alphabetical order'''
    employees = Employee.objects.order_by('last_name')
    context = {'employees': employees}
    return render(request, 'Website/employees.html', context)

def employees_detail(request, employee_id):
    '''Shows details of clicked employee'''
    employee = Employee.objects.get(id=employee_id)
    programs = Join_Training_Employee.objects.filter(employee_id=employee_id)
    context = { 'employee': employee, 'programs': programs }
    return render(request, 'Website/employees_detail.html', context)

def employees_add(request):
    ''' Directs user to the add employee form / or /
    Creates new employee record in database and redirects to employees page
    '''
    if request.method != 'POST':
      department_list = Department.objects.all().order_by('department_name')
      context = { 'department_list': department_list }
      return render(request, 'Website/employees_add.html', context)
    else:
      first = request.POST["first_name"]
      last = request.POST["last_name"]
      start = request.POST["start_date"]
      department_id = request.POST["department"]
      department = Department.objects.get(id=department_id)
      is_supervisor = request.POST["is_supervisor"]

      new_employee = Employee(first_name=first, last_name=last, start_date=start, department=department, is_supervisor=is_supervisor)
      new_employee.save()
    return HttpResponseRedirect(reverse('Website:employees'))

def employees_edit(request, employee_id):
    ''' Allows user to edit employee information:
    last name, or change department / computer / training programs assigned
    '''
    if request.method != 'POST':
      department_list = Department.objects.all()
      computer_list = Computer.objects.filter(is_available=True)
      join_list = Join_Computer_Employee.objects.filter(employee_id=employee_id, unassign_date__isnull=True)
      employee = Employee.objects.get(id=employee_id)

      all_training = Training_Program.objects.all().order_by('start_date').filter(start_date__gte=datetime.today())
      join_employee_training = Join_Training_Employee.objects.filter(employee_id=employee_id)

      context = { 'employee' : employee, 'department_list' : department_list, 'computer_list' : computer_list, 'join_list': join_list, 'all_training': all_training, 'join_employee_training': join_employee_training }

      return render(request, 'Website/employees_edit.html', context)
    else:
      employee = Employee.objects.get(id=employee_id)
      employee.first_name = request.POST["first_name"]
      employee.last_name = request.POST["last_name"]
      employee.department_id = request.POST["department"]
      employee.is_supervisor = request.POST["is_supervisor"]

      employee.save()


    return HttpResponseRedirect(reverse('Website:employees_detail', args=(employee_id,)))

def employees_edit_computer(request, employee_id):
    ''' Allows user to edit employee information:
    last name, or change department / computer / training programs assigned
    '''
    if request.method != 'POST':
      department_list = Department.objects.all()
      computer_list = Computer.objects.filter(is_available=True)
      join_list = Join_Computer_Employee.objects.filter(employee_id=employee_id, unassign_date__isnull=True)
      employee = Employee.objects.get(id=employee_id)


      context = { 'employee' : employee, 'department_list' : department_list, 'computer_list' : computer_list, 'join_list': join_list }

      return render(request, 'Website/employees_edit_computer.html', context)
    else:
      # makes current computer available again
      current_computer_relationship = Join_Computer_Employee.objects.filter(employee_id=employee_id, unassign_date__isnull=True).values()

      for computer in current_computer_relationship:
      # current_computer_to_update = Computer.objects.get(id=current_computer.computer_id)
        if computer:
          computer_to_update = Computer.objects.get(id=computer['computer_id'])
          computer_to_update.is_available = True
          computer_to_update.save()

          # get the current computer-employee relationship from the join table
          relationship = Join_Computer_Employee.objects.filter(employee_id=employee_id, unassign_date__isnull=True)
          # grab the first result (there should only be one record but you need to select it by index)
          old_computer = relationship[0]
          # set the unassigned date to today's date
          old_computer.unassign_date = datetime.today()
          old_computer.save()


      # creates new join table record with current employee and newly-selected computer
      new_computer = Join_Computer_Employee(
        assign_date= datetime.today(),
        computer_id= request.POST["unassigned_computer"],
        employee_id= employee_id
      )
      new_computer.save()

      # makes the newly-selected computer unavailable
      edited_computer_id = request.POST["unassigned_computer"]
      computer_to_update = Computer.objects.get(id=edited_computer_id)
      computer_to_update.is_available = False
      computer_to_update.save()

    return HttpResponseRedirect(reverse('Website:employees_detail', args=(employee_id,)))

def departments(request):
    '''Lists all departments sorted by name'''
    department_list = Department.objects.all().order_by('department_name')
    context = { 'department_list': department_list }
    return render(request, 'Website/departments.html', context)

def departments_detail(request, department_id):
    """Show a single department and its details"""
    department = get_object_or_404(Department, pk=department_id)
    return render(request, 'Website/departments_detail.html', {'department': department})

def departments_add(request):
    """view for adding new department"""
    if request.method != 'POST':
        return render(request, 'Website/departments_add.html')
    else:
        department_name = request.POST['department_name']
        budget = request.POST['budget']

        new_department = Department(
            department_name=department_name,
            budget=budget
            )
        new_department.save()
        return HttpResponseRedirect(reverse('Website:departments'))

def computers(request):
    '''Show a list of all computers'''
    computers = Computer.objects.order_by('manufacturer')
    context = {
        'computers': computers,
    }

    return render(request, 'Website/computers.html', context)

def computers_detail(request, computer_id):
    '''Show a single computer and its details'''
    computer = Computer.objects.get(id=computer_id)
    context = {
        'computer': computer,
        }

    return render(request, 'Website/computers_detail.html', context)

def computers_add(request):
    '''view for adding new computer'''
    if request.method != 'POST':
        return render(request, 'Website/computers_add.html')
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

def computers_delete(request, computer_id):
    '''delete computer from computer list'''

    if request.method != 'POST':
        selected_computer = Computer.objects.get(id=computer_id)
        computer_assignments = Join_Computer_Employee.objects.filter(computer_id=computer_id)

        if len(computer_assignments) == 0:
            context = {
                'selected_computer': selected_computer,
                'delete': True,
            }
        else:
            context = {
               'selected_computer': selected_computer,
                'delete': False,
            }
        return render(request, 'Website/computers_delete.html', context)
    else:
        selected_computer = Computer.objects.get(id=computer_id)
        selected_computer.delete()
        return HttpResponseRedirect(reverse('Website:computers'))

def training(request):
    ''' Gets all of the training programs from DB, sorts by most recent date,
    and filters out training programs occurring before current date '''
    training_list = Training_Program.objects.all().order_by('start_date').filter(start_date__gte=datetime.today())
    context = {'training_list': training_list}
    return render(request, 'Website/training.html', context)

def training_add(request):
    ''' Directs user to the add training program form / or /
    Creates new Training Program record in database and redirects to Training page
    '''
    if request.method != 'POST':
      return render(request, 'Website/training_add.html')
    else:
      program = request.POST["program_name"]
      description = request.POST["program_desc"]
      start = request.POST["start_date"]
      end = request.POST["end_date"]
      attendees = request.POST["max_attendees"]
      new_program = Training_Program(program_name=program, program_desc=description, start_date=start, end_date=end, max_attendees=attendees)
      new_program.save()
    return HttpResponseRedirect(reverse('Website:training'))