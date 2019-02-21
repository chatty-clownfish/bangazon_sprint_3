from rest_framework import serializers
from death_star_data.models import Customer, Product, ProductType, PaymentType, Order, ProductOrder, Department, Employee, Training, EmployeeTraining, Computer, ComputerEmployee

class TrainingSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Training
        fields = ('id', 'name', 'start_date', 'end_date', 'max_attendees', 'url')

        # TODO:  add  'employees'  to end of fields above once it is built