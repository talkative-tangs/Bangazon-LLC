from django.test import TestCase
from django.urls import reverse

import unittest

from ..models import Training_Program
# Create your tests here.

class TrainingTest(TestCase):
      ''' testing suite for Training Programs '''
      def test_list_training(self):
        new_training =  Training_Program.objects.create(
          program_name='Clerical Orientation',
          program_desc='Program will consist of answering phones, filing paperwork.',
          start_date='2019-07-11',
          end_date='2019-07-12',
          max_attendees=12,
        )

        # issue a GET request. client is a dummy web browser
        # reverse is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get(reverse('Website:training'))

        # check that the response is 200 ok
        self.assertEqual(response.status_code, 200)

        # check that rendered context contains one item
        self.assertEqual(len(response.context['training_list']), 1)

        # .encode converts from unicode to utf-8
        self.assertIn(new_training.program_name.encode(), response.content)
        self.assertIn(new_training.program_desc.encode(), response.content)
        # self.assertIn(new_training.start_date.encode(), response.content)
        # self.assertIn(new_training.end_date.encode(), response.content)
        # self.assertIn(new_training.max_attendees.encode(), response.content)
        # python encodes date string? and integer
        # print(response.content)

      def test_training_add(self):
        response = self.client.get(reverse('Website:training_add'))
        print(response)

      #   self.assertIn(response.content, 'html output goes here')