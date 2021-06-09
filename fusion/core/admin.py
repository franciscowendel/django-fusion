from django.contrib import admin
from .models import (
    Service,
    Position,
    Employee,
    Feature
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'description', 'created', 'updated', 'is_active')


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'created', 'updated', 'is_active')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'bio', 'created', 'updated', 'is_active')


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('feature', 'description', 'created', 'updated', 'is_active')
