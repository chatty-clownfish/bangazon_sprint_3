from django.shortcuts import render
from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee
from death_star_data.serializers import DepartmentSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
         'department': reverse('department', request=request, format=format),
    })

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'budget',)