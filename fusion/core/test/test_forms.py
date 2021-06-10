from django.test import TestCase
from fusion.core.forms import ContactForm


class ContactFormTestCase(TestCase):

    def setUp(self):
        self.name = 'Admin'
        self.email = 'admin@admin.com'
        self.subject = 'Hello django!'
        self.message = 'hello!'

        self.data = {
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
        }
        self.form = ContactForm(data=self.data)

    def test_send_mail(self):
        form1 = ContactForm(data=self.data)
        form1.is_valid()
        resp1 = form1.send_mail()

        form2 = self.form
        form2.is_valid()
        resp2 = form2.send_mail()
        self.assertEqual(resp1, resp2)
