from rest_framework import serializers
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductType
        fields = ('name',)

class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Product
        fields = ('title','price', 'quantity', 'product_type', 'seller')

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = ('id','name', 'account_num', 'customer','url')



class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('id','first_name','last_name','department')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    def __init__(self,*args,**kwargs):
        super(CustomerSerializer, self).__init__(*args,**kwargs)
        request = kwargs['context']['request']
        if request.query_params.get("_include") == "payments":
            self.fields["payment"] = PaymentTypeSerializer(many = True, read_only = True)
        if request.query_params.get("_include") == "products":
            self.fields["inventory"] = ProductSerializer(many = True, read_only = True) 

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'address', 'phone', 'active')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    def __init__(self,*args,**kwargs):
        super(DepartmentSerializer, self).__init__(*args,**kwargs)
        request = kwargs['context']['request']
        if request.query_params.get("_include") == "employees":
            self.fields["roster"] = EmployeeSerializer(many = True, read_only = True)

    class Meta:
        model = Department
        fields = ('id', 'name')


