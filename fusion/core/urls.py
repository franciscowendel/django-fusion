from django.urls import path
from .views import (
    IndexView,
    ServicesAPIView,
    ServiceAPIView,
    PositionsAPIView,
    PositionAPIView,
    EmployeesAPIView,
    EmployeeAPIView,
    FeaturesAPIView,
    FeatureAPIView,
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    # services
    path('services/', ServicesAPIView.as_view(), name='services'),
    path('services/<int:pk>/', ServiceAPIView.as_view(), name='service'),

    # positions
    path('positions/', PositionsAPIView.as_view(), name='positions'),
    path('positions/<int:pk>/', PositionAPIView.as_view(), name='position'),

    # employees
    path('employees/', EmployeesAPIView.as_view(), name='employees'),
    path('employees/<int:pk>/', EmployeeAPIView.as_view(), name='employee'),

    # features
    path('features/', FeaturesAPIView.as_view(), name='features'),
    path('features/<int:pk>/', FeatureAPIView.as_view(), name='feature'),

    path('positions/<int:position_pk>/employees/', EmployeesAPIView.as_view(), name='position_employees'),
    path('positions/<int:position_pk>/employees/<int:employee_pk>/', EmployeeAPIView.as_view(), name='position_employee'
         ),

]
