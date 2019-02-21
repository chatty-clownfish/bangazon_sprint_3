from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework import filters
from rest_framework.response import Response
from rest_framework.reverse import reverse

from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee
from death_star_data.serializers import PaymentTypeSerializer, CustomerSerializer



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'paymenttype': reverse('paymenttype', request=request, format=format),
        'customer': reverse('customer', request=request, format=format),
    })

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'put']

    # def get_queryset(self):
    #     query_set = Customer.objects.all()
    #     query_set_to_be_returned = []
    #     for customer in query_set:
    #         query_set_to_be_returned.append(customer.get_customer_payment)
    #         print("customer",customer.get_customer_payment, customer)
    
    #     return query_set_to_be_returned
            
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name', 'address', 'phone', 'active')