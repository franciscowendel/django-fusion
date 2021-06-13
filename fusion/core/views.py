from django.views.generic import FormView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from .models import (
    Service,
    Position,
    Employee,
    Feature,

)
from django.contrib import messages
from .forms import ContactForm

from rest_framework import generics
from .serializers import (
    ServiceSerializer,
    PositionSerializer,
    EmployeeSerializer,
    FeatureSerializer,

)
from rest_framework.generics import get_object_or_404


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
        messages.success(self.request, _('Mensagem enviada com sucesso!'))
        return super(IndexView, self).form_valid(form, *args, **kwargs)  # noqa

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar a mensagem!'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)  # noqa


# API Versão 1 usando 'generics'


class ServicesAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()  # noqa
    serializer_class = ServiceSerializer


class ServiceAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()  # noqa
    serializer_class = ServiceSerializer


class PositionsAPIView(generics.ListCreateAPIView):
    queryset = Position.objects.all()  # noqa
    serializer_class = PositionSerializer


class PositionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()  # noqa
    serializer_class = PositionSerializer


class EmployeesAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()  # noqa
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        if self.kwargs.get('service_pk'):
            return self.queryset.filter(service_id=self.kwargs.get('service_pk'))
        return self.queryset.all()


class EmployeeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()  # noqa
    serializer_class = EmployeeSerializer

    def get_object(self):
        if self.kwargs.get('service_pk'):
            return get_object_or_404(self.get_queryset(), service_id=self.kwargs.get('service_pk'),
                                     employee_pk=self.kwargs.get('employee_pk'))
        return get_object_or_404(self.get_queryset(), employee_pk=self.kwargs.get('employee_pk'))


class FeaturesAPIView(generics.ListCreateAPIView):
    queryset = Feature.objects.all()  # noqa
    serializer_class = FeatureSerializer


class FeatureAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feature.objects.all()  # noqa
    serializer_class = FeatureSerializer
