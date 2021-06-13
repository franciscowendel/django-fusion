from rest_framework import serializers
from .models import (
    Service,
    Position,
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


class PositionSerializer(serializers.ModelSerializer):

    employees = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='employee-detail')

    class Meta:

        model = Position
        fields = (
            'id',
            'position',
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
