from django.test import TestCase
from django.urls import reverse

import unittest

from ..models import Employee
from ..models import Department

# Your test suite must verify that the content of the response has one, or more, of the values that are expected. For example, if one of the employees in Fred Jackson, then your test must test that both "Fred" and "Jackson" are in the response content. Likewise for the department that the employee is assigned to.

class EmployeeTest(TestCase):
    '''Testing suite for Employee model'''

    def test_employee(self):
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

        #---Future components of employee to be tested beyond requirements--#
        # self.assertIn(new_employee.start_date.encode(), response.content)
        # self.assertIn(new_employee.end_date.encode(), response.content)
        # self.assertIn(new_employee.is_supervisor.encode(), response.content)


    def test_employee_edit(self):
        new_department = Department.objects.create(
          department_name= 'Running',
          budget=60
        )

        new_employee = Employee.objects.create(
          first_name='Forrest',
          last_name='Gump',
          start_date='1978-03-17',
          end_date='1979-02-25',
          is_supervisor=0,
          department_id=1
        )

    # =================================================
    # Testing Criteria #1
    # =================================================
    # Your test suite must verify that the content of the response has all of the required input fields.

         # reverse is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get('/website/employees/edit/1/')
        # check that the response is 200 ok
        self.assertEqual(response.status_code, 200)

        # check that each form input field is in response
        self.assertIn('<input id="first_name" type="text" name="first_name" value=Forrest required>'.encode(), response.content)
        self.assertIn('<input id="last_name" type="text" name="last_name" value=Gump required>'.encode(), response.content)
        self.assertIn('<option value="1" id="1" selected="selected">Running</option>'.encode(), response.content)
        self.assertIn('<option value=False id="is_supervisor" selected="selected">No</option>'.encode(), response.content)

    # =================================================
    # Testing Criteria 2
    # =================================================
        # Your test suite must verify that submitting the form correctly edits the employee.
        # testing edit of last name
        edit_response = self.client.post('/website/employees/edit/1/', {'first_name': 'Forrest', 'last_name': 'Drumpf', 'start_date': '1978-03-17', 'end_date': '1979-02-25', 'is_supervisor': 0, 'department': 1})

        new_employee.refresh_from_db()

        # Getting 302 back because we have a success url and the view is redirecting
        self.assertEqual(edit_response.status_code, 302)