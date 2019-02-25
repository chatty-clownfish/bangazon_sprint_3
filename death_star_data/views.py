from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse

from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee
from death_star_data.serializers import PaymentTypeSerializer, CustomerSerializer, ProductTypeSerializer, ProductSerializer, TrainingSerializers, DepartmentSerializer, EmployeeSerializer, OrderSerializer
import datetime

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'training': reverse('training', request=request, format=format),
        'employee': reverse('employee', request=request, format=format),
        'department': reverse('department', request=request, format=format),
        'ProductType' : reverse('ProductType', request = request, format = format),
        'paymenttype': reverse('paymenttype', request=request, format=format),
        'customer': reverse('customer', request=request, format=format),
        'Order': reversse('Order', request= request, format=format),
        'department': reverse('department', request=request, format=format),
    })

class TrainingViewSet(viewsets.ModelViewSet):
    '''Will get us a list of training programs as well as the ability to view a program individually.
       A list of employees who signed up for a training program will be visable.
       Able to view only programs starting today, or in the future, with the `?completed=false` query string parameter.
     '''
    queryset = Training.objects.all()
    serializer_class = TrainingSerializers
    current_date = datetime.date.today()

    def destroy(self, request, *args, **kwargs):
        query_set = self.get_object()
        if self.current_date >= query_set.end_date:
            print('LESS THAN =', query_set.end_date)
            # TODO:Make alert message to tell the user that they cannot delete past events
        elif self.current_date < query_set.end_date:
            query_set.delete()
        return query_set

    def get_queryset(self):
        ''' Assigns the keyword of completed. Then filters through our query set of training programs and evaluate
        whether current time is greater than(gte) or lesser than(lt) then return the query_set '''
        current_date = datetime.date.today()
        query_set = Training.objects.all()
        keyword = self.request.query_params.get('completed')
        if keyword == 'true':
            query_set = query_set.filter(end_date__lt=current_date)
        elif keyword == 'false':
            query_set = query_set.filter(end_date__gte=current_date)
        return query_set


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get', 'post', 'put']

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'budget')


class ProductTypeViewSet(viewsets.ModelViewSet):
    #Summary: This View Set is desplaying all of the Product Types Available through the serializer.
    #Author: Daniel Combs

    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'put']

    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'address', 'phone', 'active')

class ProductViewSet(viewsets.ModelViewSet):
    #This view set is grabbing all of the Products and using the product Serializer to help display.
    #It also alows us to look determine the filters they mey search thru.
    #Author: Daniel Combs


    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'description', 'price', 'quantity', 'product_type','seller')


class OrderViewSet(viewsets.ModelViewSet):
    # This view set is grabbing all of the Products and using the product Serializer to help display.
    #It also alows us to look determine the filters they mey search thru.
    #Author: Daniel Combs

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('payment_type', 'product', 'customer', 'url')

    def get_queryset(self):
        query_set = Order.objects.all()
        keyword = self.request.query_params.get('completed')
        if keyword == 'true':
            query_set = query_set.exclude(payment_type_id__isnull=True)
        elif keyword == 'false':
            query_set =query_set.exclude(payment_type_id__isnull=False)
        return query_set