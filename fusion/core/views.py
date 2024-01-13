from django.views.generic import FormView
from django.urls import reverse_lazy
from .models import (
    Service,
    Role,
    Employee,
    Feature,

)
from django.contrib import messages
from .forms import ContactForm

from rest_framework import generics
from .serializers import (
    ServiceSerializer,
    RoleSerializer,
    EmployeeSerializer,
    FeatureSerializer,

)
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins

from rest_framework.decorators import action
from rest_framework.response import Response
from .permissions import (
    EsuperUserPost,
    EsuperUserPut,
    EsuperUserDelete,
)
from rest_framework import permissions


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
        messages.success(self.request, 'Message sent successfully!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)  # noqa

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error sending message!')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)  # noqa


# API Version 1 using 'generics'


class ServicesAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()  # noqa
    serializer_class = ServiceSerializer


class ServiceAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()  # noqa
    serializer_class = ServiceSerializer


class RolesAPIView(generics.ListCreateAPIView):
    queryset = Role.objects.all()  # noqa
    serializer_class = RoleSerializer


class RoleAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()  # noqa
    serializer_class = RoleSerializer


class EmployeesAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()  # noqa
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        if self.kwargs.get('role_pk'):
            return self.queryset.filter(role_id=self.kwargs.get('role_pk'))
        return self.queryset.all()


class EmployeeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()  # noqa
    serializer_class = EmployeeSerializer

    def get_object(self):
        if self.kwargs.get('role_pk'):
            return get_object_or_404(self.get_queryset(), role_id=self.kwargs.get('role_pk'),
                                     pk=self.kwargs.get('employee_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('employee_pk'))


class FeaturesAPIView(generics.ListCreateAPIView):
    queryset = Feature.objects.all()  # noqa
    serializer_class = FeatureSerializer


class FeatureAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feature.objects.all()  # noqa
    serializer_class = FeatureSerializer


# API version 2 using 'viewsets'


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()  # noqa
    serializer_class = ServiceSerializer


class RoleViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.DjangoModelPermissions,
        EsuperUserPost,
        EsuperUserPut,
        EsuperUserDelete,
    )
    queryset = Role.objects.all()  # noqa
    serializer_class = RoleSerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):  # noqa
        self.pagination_class.page_size = 1
        employees = Employee.objects.filter(role_id=pk)  # noqa
        page = self.paginate_queryset(employees)

        if page is not None:
            serializer = EmployeeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)


# API  versão 2 usando 'mixins'

class EmployeeViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Employee.objects.all()  # noqa
    serializer_class = EmployeeSerializer


class FeatureViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Feature.objects.all()  # noqa
    serializer_class = FeatureSerializer
