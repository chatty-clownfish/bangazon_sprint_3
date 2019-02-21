from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view

from rest_framework import filters

from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee
from death_star_data.serializers import 



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
         
    })