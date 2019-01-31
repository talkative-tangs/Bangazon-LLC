from django.test import TestCase
from django.urls import reverse

import unittest

from ..models import Department
# Create your tests here.

# Your test suite must verify that the content of the response has one,
# or more, of the expected values. For example, 
# if one of the departments in your database is "Sales", 
# then you must verify that it exists in the content.

class DepartmentTest(TestCase):
    ''' testing suite for Departments'''
    def test_lists_departments(self):
        new_department = Department.objects.create(
            department_name="Invisible Pants for Men that Enjoy Ferris Wheels",
            budget=32
        )

        new_department2 = Department.objects.create(
            department_name="Socks for Babies with Extra Toes",
            budget=8
        )

        new_department3 = Department.objects.create(
            department_name="Sales of Raccoons that Think They Are Dogs",
            budget=1000
        )

        #issue a get request
        #client is a dummy web browser
        #reverse used to generate a url for given view
        #dont have to hard code routes into code
        response = self.client.get(reverse('Website:departments'))

        #check that the response is 200 ok
        self.assertEqual(response.status_code, 200)

        #check that rendered content contains 3 department
        #response.context is content variable passed to template
        #we know id will be 3 because it is adding to fake db
        #department_list is key in view
        self.assertEqual(len(response.context['department_list']), 3)

        # .encode converts from unicode to utf-8
        #example:
        #if string is python
        #the encoded version is b'pyth\xc3\xb6n
        #content is finished/ready to send to the browser html
        self.assertIn(new_department.department_name.encode(), response.content)
        self.assertIn(new_department2.department_name.encode(), response.content)
        self.assertIn(new_department3.department_name.encode(), response.content)

        #specific test department name ?? 

    def test_post_department(self):
        '''Your test suite must verify that when a POST operation is performed to the corresponding URL, 
        then a successful response is received (i.e. status code must be 200)'''

        response = self.client.post(reverse('Website:departments_add'), 
            {
            'department_name': 'Organically Grown Pasta-made Blouses',
            'budget': 2
            })

        get_response = self.client.get(reverse('Website:departments'))

        # getting 302 back because we have a successful url and the view is redirecting
        self.assertEqual(response.status_code, 302)
        # get a 200 when checking the list of computers and new computer exists
        self.assertEqual(get_response.status_code, 200)
    
    def test_get_department_form(self):
        '''Your test suite must verify that the content of the response has the required input fields.'''
        response = self.client.get(reverse('Website:departments_add'))

        self.assertIn(
            '<input type="text" name="department_name" required/>'.encode(), response.content
        )
    
    def test_get_department_detail(self):
        new_department = Department.objects.create(
            department_name = "Corgi Fur Extractors",
            budget = 900
        )

        response = self.client.get(reverse('Website:departments_detail', args=(1,)))
        self.assertEqual(response.context["department"].department_name, new_department.department_name)