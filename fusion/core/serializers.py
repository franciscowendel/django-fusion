from rest_framework import serializers
from .models import (
    Service,
    Role,
    Employee,
    Feature,
)


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = (
            'id',
            'service',
            'description',
            'created',
            'updated',
            'is_active',
        )


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            'id',
            'name',
            'position',
            'bio',
            'facebook',
            'twitter',
            'instagram',
            'created',
            'updated',
            'is_active',
        )


class RoleSerializer(serializers.ModelSerializer):
    # Nested Relationship
    # employees = EmployeeSerializer(many=True, read_only=True)

    # Primary Key Related Field
    # employees = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    # Hyper Linked Related Field
    employees = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='employee-detail')

    class Meta:

        model = Role
        fields = (
            'id',
            'role',
            'created',
            'updated',
            'is_active',
            'employees',
        )


class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        fields = (
            'id',
            'feature',
            'description',
            'created',
            'updated',
            'is_active',
        )
