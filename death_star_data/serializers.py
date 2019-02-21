from rest_framework import serializers
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee



class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = PaymentType
    fields = ('name', 'account_num', 'customer')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    
  class Meta:
    model = Customer
    fields = ('first_name', 'last_name', 'address', 'phone', 'active')

