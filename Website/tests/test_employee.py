from django.test import TestCase
from django.urls import reverse

import unittest

from ..models import Employee

# Your test suite must verify that the content of the response has one, or more, of the values that are expected. For example, if one of the employees in Fred Jackson, then your test must test that both "Fred" and "Jackson" are in the response content. Likewise for the department that the employee is assigned to.

class EmployeeTest(TestCase):
  '''Testing suite for Employee model'''