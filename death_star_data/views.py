from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework import filters
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee
from death_star_data.serializers import TrainingSerializers



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
         'training': reverse('training', request=request, format=format),
    })

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializers

    def delete(self, pk, request):
        password = request.data.get('password')
        article_id = request.data.get('article')
        article_instance = article.objects.get(id=article_id)
        if password == article_instance.password:
            article_instance.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_304_NOT_MODIFIED)