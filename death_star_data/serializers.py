from rest_framework import serializers
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee


class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    # This is the Serializer for the Model of product Type
    # Author: Daniel Combs

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
    # This serializer is looking at the product model,
    # and showing what all is going to be displayed in the fields section.
    # Author: Daniel Combs


  class Meta:
    model = Product
    fields = ('title', 'description', 'price', 'quantity', 'product_type','seller')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    #This serializer is looking at the product model,
    #and showing what all is going to be displayed in the fields section.
    #Author: Daniel Combs

  class Meta:
    model = Order
    fields = ('payment_type', 'product', 'customer')