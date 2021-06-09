from django.views.generic import FormView
from django.urls import reverse_lazy
from .models import (
    Service,
    Employee,
    Feature,

)
from .forms import ContactForm


class IndexView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index')
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()  # noqa
        context['employess'] = Employee.objects.order_by('?').all()  # noqa
        context['features'] = Feature.objects.order_by('?').all()  # noqa
        return context
