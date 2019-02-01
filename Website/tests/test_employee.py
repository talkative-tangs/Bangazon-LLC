from django.test import TestCase
from django.urls import reverse

import unittest

from ..models import Employee
from ..models import Department
from ..models import Training_Program
from ..models import Join_Training_Employee
from ..models import Computer
from ..models import Join_Computer_Employee


class EmployeeTest(TestCase):
    '''Testing suite for Employee model'''

    # =================================================
    # Testing Criteria Issue #1
    # =================================================
      # Your test suite must verify that the content of the response has one, or more, of the values that are expected. For example, if one of the employees in Fred Jackson, then your test must test that both "Fred" and "Jackson" are in the response content. Likewise for the department that the employee is assigned to.

    def test_employee(self):
        '''Test creation of employee. Your test suite must verify that the content of the response has one, or more, of the values that are expected.'''

        new_department = Department.objects.create(
            id=2,
            department_name= 'Running',
            budget=60
            )

        new_employee = Employee.objects.create(
            first_name='Forrest',
            last_name='Gump',
            start_date='1978-03-17',
            end_date='1979-02-25',
            is_supervisor=0,
            department_id=2
            )

        # issue a GET request. client is a dummy web browser
        # reverse is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get(reverse('Website:employees'))

        # check that the response is 200 ok
        self.assertEqual(response.status_code, 200)

        # check that rendered context contains matching value
        self.assertEqual(len(response.context['employees']), 1)

        # .encode converts from unicode to utf-8
        self.assertIn(new_employee.first_name.encode(), response.content)
        self.assertIn(new_employee.last_name.encode(), response.content)
        self.assertIn(new_department.department_name.encode(), response.content)

        #---Future components of employee to be tested beyond issue #1 requirements--#
        # self.assertIn(new_employee.start_date.encode(), response.content)
        # self.assertIn(new_employee.end_date.encode(), response.content)
        # self.assertIn(new_employee.is_supervisor.encode(), response.content)


    # def test_employee_edit(self):
    #     new_department = Department.objects.create(
    #       department_name= 'Running',
    #       budget=60
    #     )

    #     new_employee = Employee.objects.create(
    #       first_name='Forrest',
    #       last_name='Gump',
    #       start_date='1978-03-17',
    #       end_date='1979-02-25',
    #       is_supervisor=0,
    #       department_id=1
    #     )

    # # =================================================
    # # Testing Criteria #1
    # # =================================================
    # # Your test suite must verify that the content of the response has all of the required input fields.

    #      # reverse is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
    #     response = self.client.get('/website/employees/edit/1/')
    #     # check that the response is 200 ok
    #     self.assertEqual(response.status_code, 200)

    #     # check that each form input field is in response
    #     self.assertIn('<input id="first_name" type="text" name="first_name" value=Forrest required>'.encode(), response.content)
    #     self.assertIn('<input id="last_name" type="text" name="last_name" value=Gump required>'.encode(), response.content)
    #     self.assertIn('<option value="1" id="1" selected="selected">Running</option>'.encode(), response.content)
    #     self.assertIn('<option value=False id="is_supervisor" selected="selected">No</option>'.encode(), response.content)

    # # =================================================
    # # Testing Criteria 2
    # # =================================================
    #     # Your test suite must verify that submitting the form correctly edits the employee.
    #     # testing edit of last name
    #     edit_response = self.client.post('/website/employees/edit/1/', {'first_name': 'Forrest', 'last_name': 'Drumpf', 'start_date': '1978-03-17', 'end_date': '1979-02-25', 'is_supervisor': 0, 'department': 1})

    #     new_employee.refresh_from_db()

    #     # Getting 302 back because we have a success url and the view is redirecting
    #     self.assertEqual(edit_response.status_code, 302)

    # =================================================
    # Testing Criteria Issue #3
    # =================================================

    def test_employee_detail(self):
        '''Your test suite must verify that the content of the response has all of the expected values of the employee - name, department, computer, and training programs.'''

# ------------Dummy Data for test suite----------------

        new_department = Department.objects.create(
            id=2,
            department_name= 'Running',
            budget=60
        )

        new_employee = Employee.objects.create(
            id=1,
            first_name='Forrest',
            last_name='Gump',
            start_date='1978-03-17',
            end_date='1979-02-25',
            is_supervisor=0,
            department_id=2
        )

        new_computer = Computer.objects.create(
            id=6,
            deleted=None,
            purchase_date='1977-04-24',
            decommission_date=None,
            manufacturer='Apple',
            model='Macintosh',
            is_available=0
        )

        new_computer2 = Computer.objects.create(
            id=8,
            deleted=None,
            purchase_date='1977-04-24',
            decommission_date=None,
            manufacturer='Apple',
            model='Macintosh',
            is_available=0
        )

    # Current Computer
        new_computer_employee = Join_Computer_Employee.objects.create(
            id=1,
            assign_date='1978-07-16',
            unassign_date=None,
            computer_id=6,
            employee_id=1
        )

    #Previous Computer
        new_computer_employee2 = Join_Computer_Employee.objects.create(
            id=2,
            assign_date='1978-03-17',
            unassign_date='1978-07-16',
            computer_id=8,
            employee_id=1
        )

    # Past Training Program
        new_training = Training_Program.objects.create(
            deleted=None,
            program_name='Buying Chocolates',
            program_desc='Mama always said',
            start_date='1978-09-11',
            end_date='1978-09-12',
            max_attendees=15
        )
    # Future Training Program
        new_training2 = Training_Program.objects.create(
            deleted=None,
            program_name='Future Lt. Dan',
            program_desc='No legs',
            start_date='2019-09-11',
            end_date='2019-09-12',
            max_attendees=15
        )
    # Employee's training programs
        new_training_employee = Join_Training_Employee.objects.create(
            employee_id=1,
            training_program_id=1
        )

        new_training_employee2 = Join_Training_Employee.objects.create(
            employee_id=1,
            training_program_id=2
        )
    # End Employee's training programs

# ------------End Dummy Data for test suite----------------

        response = self.client.get(reverse('Website:employees_detail', args=(1,)))
        self.assertEqual(response.context["employee"].first_name, new_employee.first_name)
        self.assertEqual(response.context["employee"].last_name, new_employee.last_name)
        self.assertEqual(response.context["employee"].department_id, new_employee.department_id)
        self.assertEqual(response.context["employee"].current_computer, f"#{new_computer.id}")
        self.assertEqual(response.context["programs"][0].training_program.id, new_training_employee.training_program_id)
        self.assertEqual(response.context["programs"][1].training_program.id, new_training_employee2.training_program_id)



