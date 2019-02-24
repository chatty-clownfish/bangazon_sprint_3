from rest_framework import serializers
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
'''
Summary: This is the Serializer for the Model of product Type

Author: Daniel Combs
'''
    class Meta:
        model = ProductType
        fields = ('name',)




class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = PaymentType
    fields = ('name', 'account_num', 'customer')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Customer
    fields = ('first_name', 'last_name', 'address', 'phone', 'active')

class ProductSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Product
    fields = ('title', 'description', 'price', 'quantity', 'product_type','seller')
