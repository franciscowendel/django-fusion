from django.urls import path
from .views import (
    IndexView,

    ServicesAPIView,
    ServiceAPIView,

    RolesAPIView,
    RoleAPIView,

    EmployeesAPIView,
    EmployeeAPIView,

    FeaturesAPIView,
    FeatureAPIView,

    ServiceViewSet,
    RoleViewSet,
    EmployeeViewSet,
    FeatureViewSet,
)

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('services', ServiceViewSet)
router.register('roles', RoleViewSet)
router.register('employees', EmployeeViewSet)
router.register('features', FeatureViewSet)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    # services
    path('services/', ServicesAPIView.as_view(), name='services'),
    path('services/<int:pk>/', ServiceAPIView.as_view(), name='service'),

    # positions
    path('roles/', RolesAPIView.as_view(), name='roles'),
    path('roles/<int:pk>/', RoleAPIView.as_view(), name='role'),

    # employees
    path('employees/', EmployeesAPIView.as_view(), name='employees'),
    path('employees/<int:employee_pk>/', EmployeeAPIView.as_view(), name='employee'),

    # features
    path('features/', FeaturesAPIView.as_view(), name='features'),
    path('features/<int:pk>/', FeatureAPIView.as_view(), name='feature'),

    path('roles/<int:role_pk>/employees/', EmployeesAPIView.as_view(), name='role_employees'),
    path('roles/<int:role_pk>/employees/<int:employee_pk>/', EmployeeAPIView.as_view(), name='role_employee'
         ),

]
