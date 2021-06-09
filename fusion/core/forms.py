from django import forms
from django.core.mail import EmailMessage


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=120)
    email = forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=150)
    message = forms.CharField(label='Message', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}'

        mail = EmailMessage(
            subject=subject,
            body=content,
            from_email='fusion@gmail.com',
            to=['fusion@gmail.com', ],
            headers={'Reply-to': email}
        )
        mail.send()
