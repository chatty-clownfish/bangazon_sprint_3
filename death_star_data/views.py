from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee
from death_star_data.serializers import TrainingSerializers
import datetime



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
         'training': reverse('training', request=request, format=format),
    })


class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializers
    

    def get_queryset(self):
        current_date = datetime.date.today()
        query_set = Training.objects.all()
        keyword = self.request.query_params.get('completed')
        if keyword == 'true':    
            print("query params", keyword)
            print("HERE", current_date)
            query_set = query_set.filter(end_date__lt=current_date)
        elif keyword == 'false':
            query_set = query_set.filter(end_date__gte=current_date)
        return query_set
    

    
    


  

    
        