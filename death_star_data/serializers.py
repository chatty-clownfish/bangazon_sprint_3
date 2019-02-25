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

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    '''The following variable connects the FK of department on the employee model, which gives access to employee information through the serializer using many=True.

    More about nested relationships here: https://www.django-rest-framework.org/api-guide/relations/#nested-relationships'''
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ('id', 'name', 'budget', 'url', 'employees')

