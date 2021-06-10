from django.views.generic import FormView
from django.urls import reverse_lazy
from .models import (
    Service,
    Employee,
    Feature,

)
from django.contrib import messages
from .forms import ContactForm


class IndexView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()  # noqa
        context['employees'] = Employee.objects.order_by('?').all()  # noqa
        context['features'] = Feature.objects.order_by('?').all()  # noqa
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Mensagem enviada com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)  # noqa

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar a mensagem!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)  # noqa
