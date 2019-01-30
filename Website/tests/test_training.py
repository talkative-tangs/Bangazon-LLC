from django.test import TestCase
from django.urls import reverse
import unittest

from ..models import Training_Program

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

        # issue a GET request.
        response = self.client.get(reverse('Website:training'))

        # check that the response is 200 ok
        self.assertEqual(response.status_code, 200)

        # check that rendered context contains one item
        self.assertEqual(len(response.context['training_list']), 1)

        #  checks that the response context equals what was sent
        # self.assertEqual(response.context['training_list'], new_training)

        # .encode converts from unicode to utf-8
        self.assertIn(new_training.program_name.encode(), response.content)
        self.assertIn(new_training.program_desc.encode(), response.content)
        # self.assertIn('July 11, 2019', response.content)
        # self.assertIn(new_training.end_date.encode(), response.content)
        # self.assertIn(new_training.max_attendees.encode(), response.content)
        # python encodes date string? and integer
        # print(response.content)
        # print(response.content)

      def test_training_add(self):
        response = self.client.get(reverse('Website:training_add'))
        # print(response)

      #   self.assertIn(response.content, 'html output goes here')