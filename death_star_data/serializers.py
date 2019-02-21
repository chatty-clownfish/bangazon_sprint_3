from rest_framework import serializers
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = ('name', 'budget')
