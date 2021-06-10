from django.test import TestCase, Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.data = {
            'name': 'Admin',
            'email': 'admin@admin.com',
            'subject': 'Hello django!',
            'message': 'hello!'
        }
        self.client = Client()

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.data)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        request = self.client.post(reverse_lazy('index'), data={'name': 'Test', 'email': 'test@test.com'})
        self.assertEqual(request.status_code, 200)
