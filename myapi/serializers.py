from .models import Employee, Car
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

