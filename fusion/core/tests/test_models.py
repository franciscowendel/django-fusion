import uuid

from django.test import TestCase
from fusion.core.models import shuffle_filename
from model_bakery import baker


class ShuffleFilenameTestCase(TestCase):

    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_shuffle_filename(self):
        file = shuffle_filename(None, 'tests.png')
        self.assertTrue(len(file), len(self.filename))


class ServiceTestCase(TestCase):

    def setUp(self):
        self.service = baker.make('Service')

    def test_str(self):
        self.assertEqual(str(self.service), self.service.service)


class PositionTestCase(TestCase):

    def setUp(self):
        self.position = baker.make('Position')

    def test_str(self):
        self.assertEqual(str(self.position), self.position.position)


class EmployeeTestCase(TestCase):

    def setUp(self):
        self.employee = baker.make('Employee')

    def test_str(self):
        self.assertEqual(str(self.employee), self.employee.name)


class FeatureTestCase(TestCase):

    def setUp(self):
        self.feature = baker.make('Feature')

    def test_str(self):
        self.assertEqual(str(self.feature), self.feature.feature)
