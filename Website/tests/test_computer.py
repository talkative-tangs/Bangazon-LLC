from django.test import TestCase
from django.urls import reverse

import unittest

from ..models import Computer



class ComputerTest(TestCase):
    '''Testing for Computers'''

    def test_computers(self):
        new_computer = Computer.objects.create(
            purchase_date="2019-01-01",
            decommission_date="2019-01-29",
            manufacturer="Awesome Computer",
            model="Best Eva",
            is_available=True,
        )

        #issue a get request
        #client is a dummy web browser
        #reverse used to generate a url for given view
        #dont have to hard code routes into code
        response = self.client.get(reverse('Website:computers'))

        #check that the response is 200 ok
        self.assertEqual(response.status_code, 200)

        #check that rendered content contains a computer
        self.assertEqual(len(response.context['computers']), 1)

        # .encode converts from unicode to utf-8
        self.assertIn(new_computer.manufacturer.encode(), response.content)
        
        
# =================================================
# Testing Criteria #1
# =================================================

    def test_computers_add(self):
        '''Your test suite must verify that the content of the responses contain all required input fields, where appropriate.'''
        
        response = self.client.get(reverse('Website:computers_add'))

        self.assertIn(
            '<input type="text" name="manufacturer" required/>'.encode(), response.content)
        self.assertIn(
            '<input type="text" name="model" required/>'.encode(), response.content)
        self.assertIn(
            '<input type="date" name="purchase_date" required/>'.encode(), response.content)


# =================================================
# Testing Criteria 2
# =================================================

    def test_post_computer(self):
        '''Your test suite must verify that when a POST operation is performed to the corresponding URL, then a successful response is received. Status code must be 200.'''

        response = self.client.post(reverse('Website:computers_add'), 
            {
            'manufacturer': 'Apple',
            'model': 'Macbook Pro',
            'purchase_date': '2019-01-29',
            })

        get_response = self.client.get(reverse('Website:computers'))

        # getting 302 back because we have a successful url and the view is redirecting
        self.assertEqual(response.status_code, 302)
        # get a 200 when checking the list of computers and new computer exists
        self.assertEqual(get_response.status_code, 200)



# =================================================
# Testing Criteria #3
# =================================================

    def test_delete_computer(self):
        '''Your test suite must verify that when a DELETE operation is performed to the corresponding URL, then a successful response is received. Status code must be 200'''

        response = self.client.post(reverse('Website:computers_add'), 
            {
            'manufacturer': 'Apple',
            'model': 'Macbook Pro',
            'purchase_date': '2019-01-29',
            })

        get_response = self.client.post(reverse('Website:computers_delete', args=(1,)))

        # getting 302 back because we have a successful url and the view is redirecting
        self.assertEqual(response.status_code, 302)
        # check that computer is deleted
        computer = Computer.objects.filter(id=1)
        self.assertEqual(len(computer), 0)
        # return to list of computers
        final_get_response = self.client.get(reverse('Website:computers'))
        # check the list for a final 200 response
        self.assertEqual(final_get_response.status_code, 200)

