from rest_framework import serializers
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee

'''

Ticket #7

* If the query string parameter of `?_include=employees` is provided, then all employees in the department(s) should be included in the response.
* If the query string parameters of `?_filter=budget&_gt=300000` is provided on a request for the list of departments, then any department whose budget is $300,000, or greater, should be in the response.

'''

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'start_date', 'is_supervisor', 'department')

class TrainingSerializers(serializers.HyperlinkedModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)
    class Meta:
        model = Training
        fields = ('id', 'name', 'start_date', 'end_date', 'max_attendees', 'employees', 'url')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    '''The following variable connects the FK of department on the employee model, which gives access to employee information through the serializer using many=True.

    More about nested relationships here: https://www.django-rest-framework.org/api-guide/relations/#nested-relationships'''
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'budget', 'url', 'employees')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    # This is the Serializer for the Model of product Type
    # Author: Daniel Combs

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
  product = ProductSerializer(many = True, source = 'product.all', read_only = True)
  class Meta:
    model = Order
    fields = ('payment_type', 'product', 'customer')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    def __init__(self,*args,**kwargs):
        super(DepartmentSerializer, self).__init__(*args,**kwargs)
        request = kwargs['context']['request']
        if request.query_params.get("_include") == "employees":
            self.fields["roster"] = EmployeeSerializer(many = True, read_only = True)

    class Meta:
        model = Department
        fields = ('id', 'name')


