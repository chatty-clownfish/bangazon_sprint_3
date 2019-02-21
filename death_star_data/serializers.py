from rest_framework import serializers
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee


class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = ('id','name', 'account_num', 'customer','url')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    payment = PaymentTypeSerializer(many = True, read_only = True)

    class Meta:
        model = Customer
        fields = ('id','first_name', 'last_name', 'address', 'phone','active','url', 'payment')




