from rest_framework import serializers
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee



class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'start_date', 'is_supervisor', 'department')
        # fields = "__all__"

class TrainingSerializers(serializers.HyperlinkedModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)
    class Meta:
        model = Training
        fields = ('id', 'name', 'start_date', 'end_date', 'max_attendees', 'employees', 'url')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    '''The following variable connects the FK of department on the employee model, which gives access to employee information through the serializer using many=True.

    More about nested relationships here: https://www.django-rest-framework.org/api-guide/relations/#nested-relationships'''

    # employees = EmployeeSerializer(many=True, read_only=True)
    def __init__(self,*args,**kwargs):
        super(DepartmentSerializer, self).__init__(*args,**kwargs)
        request = kwargs['context']['request']
        include = request.query_params.get("_include", None)

        if include == 'employees':
            self.fields['roster'] = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    # This is the Serializer for the Model of product Type
    # Author: Daniel Combs

    class Meta:
        model = ProductType
        fields = ('name',)

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # This serializer is looking at the product model,
    # and showing what all is going to be displayed in the fields section.
    # Author: Daniel Combs


  class Meta:
    model = Product
    fields = ('title', 'description', 'price', 'quantity', 'product_type','seller')

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PaymentType
        fields = ('id','name', 'account_num', 'customer','url')

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



class OrderSerializer(serializers.HyperlinkedModelSerializer):
    #This serializer is looking at the product model,
    #and showing what all is going to be displayed in the fields section.
    #Author: Daniel Combs
  product = ProductSerializer(many = True, source = 'product.all', read_only = True)

  def __init__(self,*args,**kwargs):
    super(OrderSerializer, self).__init__(*args,**kwargs)
    request = kwargs['context']['request']
    include = request.query_params.get("_include", None)

    if include:
      if 'products' in include:
          self.fields['product'] = ProductSerializer(many=True, read_only=True)

      if 'customers' in include:
          self.fields['customer'] = CustomerSerializer(read_only=True, context=self.context)

  class Meta:
    model = Order
    fields = ('payment_type', 'product', 'customer')

class ComputerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Computer
        fields = ('id', 'purchase_date', 'decommission_date', 'manufacturer', 'model', 'employee', 'url')

