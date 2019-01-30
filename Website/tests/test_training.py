from django.test import TestCase
from django.urls import reverse
import unittest

from ..models import Training_Program

class TrainingTest(TestCase):
      ''' Testing suite for Training Programs '''
      def test_list_training(self):
        new_training =  Training_Program.objects.create(
          program_name='Clerical Orientation',
          program_desc='Program will consist of answering phones, filing paperwork.',
          start_date='2019-07-11',
          end_date='2019-07-12',
          max_attendees=12,
        )

        # issue a GET request.
        response = self.client.get(reverse('Website:training'))

        # check that the response is 200 ok
        self.assertEqual(response.status_code, 200)

        # check that rendered context contains one training program
        self.assertEqual(len(response.context['training_list']), 1)

        # .encode converts from unicode to utf-8
        self.assertIn(new_training.program_name.encode(), response.content)

# =================================================
# Testing Criteria #1
# =================================================

      def test_training_add(self):
        ''' Your test suite must verify that the content of the responses contain all required input fields, where a form is requested. '''
        response = self.client.get(reverse('Website:training_add'))

        self.assertIn(
            '<input id="program_name" type="text" name="program_name" required>'.encode(), response.content)
        self.assertIn(
            '<input id="program_desc" type="text" name="program_desc" required>'.encode(), response.content)
        self.assertIn(
            '<input id="start_date" type="date" name="start_date" required>'.encode(), response.content)
        self.assertIn(
            '<input id="end_date" type="date" name="end_date" required>'.encode(), response.content)
        self.assertIn(
            '<input id="max_attendees" type="number" name="max_attendees" required>'.encode(), response.content)


# =================================================
# Testing Criteria 2
# =================================================

      def test_training_post(self):
        '''Your test suite must verify that when a POST operation is performed to the corresponding URL, then a successful response is received. Status code must be 200.'''

        response = self.client.post(reverse('Website:training_add'),
            {
            'program_name': 'Testing Training',
            'program_desc': 'Dummy text for the Testing Training program',
            'start_date': '2019-04-29',
            'end_date': '2019-05-02',
            'max_attendees': 11,
            })

        get_response = self.client.get(reverse('Website:training'))

        # getting 302 back because we have a successful url and the view is redirecting
        self.assertEqual(response.status_code, 302)
        # get a 200 when checking the list of training and new training program exists
        self.assertEqual(get_response.status_code, 200)
