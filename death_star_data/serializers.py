from rest_framework import serializers
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        fields = ('name',)



class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = ('id','name', 'account_num', 'customer','url')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    def __init__(self,*args,**kwargs):
        super(CustomerSerializer, self).__init__(*args,**kwargs)
        request = kwargs['context']['request']
        if request.query_params.get("_include") == "payment":
            self.fields["payment"] = PaymentTypeSerializer(many = True, read_only = True)

    class Meta:
        model = Customer
        fields = "__all__"

        



  class Meta:
    model = Customer
    fields = ('first_name', 'last_name', 'address', 'phone', 'active')

class ProductSerializer(serializers.HyperlinkedModelSerializer):

  class Meta:
    model = Product
    fields = ('title', 'description', 'price', 'quantity', 'product_type','seller')
