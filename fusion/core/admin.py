from django.contrib import admin
from .models import (
    Service,
    Role,
    Employee,
    Feature
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'description', 'created', 'updated', 'is_active')


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'created', 'updated', 'is_active')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'bio', 'created', 'updated', 'is_active')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature', 'description', 'created', 'updated', 'is_active')
