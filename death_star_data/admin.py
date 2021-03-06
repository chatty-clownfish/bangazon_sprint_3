from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(PaymentType)
admin.site.register(Order)
admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Training)
admin.site.register(EmployeeTraining)
admin.site.register(Computer)
admin.site.register(ComputerEmployee)
admin.site.register(ProductOrder)