# Live coded (LiveShare) as team: Ousama, Bryan, Lesley, Elyse

from django.db import models
from datetime import datetime, date

from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE

# Create your models here.
# Models created to initialize database.

# Department Model
class Department(models.Model):
    """a grouping of employees"""
    department_name = models.CharField(max_length=100)
    budget = models.IntegerField()

    #getter method
    #logic you want that has more to do with the model than the view
    @property
    def current_employees(self):
        # print("self", self.budget)
        return len(self.employee_set.filter(end_date__isnull=True))

    def __str__(self):
        return self.department_name

# Employee Model
class Employee(models.Model):
    """a person that works for the company"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField('Starting Date')
    end_date = models.DateField('Ending Date', default=None, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    is_supervisor = models.BooleanField(default=False)

    @property
    def current_computer(self):
        if self.join_computer_employee_set.filter(unassign_date__isnull=True).exists() == True:
            computer = self.join_computer_employee_set.filter(unassign_date__isnull=True).values_list('computer_id')
            computer_number = ' '.join(map(str, computer[0]))
            return f"#{computer_number}"
        else:
            return "No computer currently assigned."

    def __str__(self):
        return_value = (f"{self.first_name} {self.last_name} works in the {self.department} department")
        return return_value

#Computer Model
class Computer(SafeDeleteModel):
    """A device that is assigned to a company employee"""
    _safedelete_policy = SOFT_DELETE_CASCADE

    purchase_date = models.DateField('Purchase Date')
    decommission_date = models.DateField('Decommission Date', default=None, blank=True, null=True)
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    is_available = models.BooleanField(default=True)
    employee = models.ManyToManyField(Employee, through='Join_Computer_Employee')

    def __str__(self):
        computer_name = (f"{self.manufacturer} {self.model} - ID#{self.id}")
        return computer_name

# Join table for Computer & Employee
class Join_Computer_Employee(models.Model):
    """a relationship between computers and employees"""
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT)
    computer = models.ForeignKey('Computer', on_delete=models.PROTECT)
    assign_date = models.DateField('Assign Date')
    unassign_date = models.DateField('Unassign Date', default=None, blank=True, null=True)

# Training Program Model
class Training_Program(SafeDeleteModel):
    """A program the company offers employees"""
    _safedelete_policy = SOFT_DELETE_CASCADE

    program_name = models.CharField(max_length=100)
    program_desc = models.CharField(max_length=200)
    start_date = models.DateField('Starting Date')
    end_date = models.DateField('Ending Date')
    max_attendees =  models.IntegerField()
    employee = models.ManyToManyField(Employee, through='Join_Training_Employee')

    @property
    def has_ended(self):
        if date.today() > self.end_date:
          return True
        else:
          return False

    def __str__(self):
        """returns a training program name"""
        return self.program_name

# Join table for Training Program & Employee
class Join_Training_Employee(models.Model):
    """The join table for employees and training"""
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT)
    training_program = models.ForeignKey('Training_Program', on_delete=models.PROTECT)
