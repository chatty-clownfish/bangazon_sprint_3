from django.db import models

# Create your models here.
class Customer(models.Model):
    '''A Bangazon customer'''
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField(blank=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        '''string method that returns the customer's full name'''

        return f"{self.first_name} {self.last_name}"


class ProductType(models.Model):
    '''Various Product Categories'''
    name =  models.CharField(max_length=50, blank=False)

    def __str__(self):
        '''string method that returns the product type name'''

        return self.name

class Product(models.Model):
    '''An item that a User can Sell or Buy'''

    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    quantity = models.IntegerField(blank=False)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True)
    seller = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='inventory')

    def __str__(self):
        '''string method that returns the Product title'''

        return self.title

class PaymentType(models.Model):
    '''A payment type saved by the buyer for use with orders'''

    name = models.CharField(max_length=50, blank=False)
    account_num = models.IntegerField(blank=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='payment')

    def __str__(self):
        '''string method that returns the payment type name'''

        return self.name

class Order(models.Model):
    '''An order placed by the buying/logged in user'''

    payment_type = models.ForeignKey(PaymentType, default=None, blank=True, null=True, on_delete=models.PROTECT)
    product = models.ManyToManyField(Product, through='ProductOrder')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        '''string method that returns the Order id'''

        return str(self.id)

class ProductOrder(models.Model):
    '''A join table linking the product being sold to the order being placed'''
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        '''string method that returns the ProductOrder id'''

        return str(self.id)

class Department(models.Model):
    name = models.CharField(default="", max_length=100)
    budget = models.IntegerField()
    

    def __str__(self):
        return f"Name: {self.name}  Budget: {self.budget}"

class Employee(models.Model):
    '''An instance of a Bangazon Employee'''
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    start_date = models.DateField()
    is_supervisor = models.BooleanField()
    '''related_name on the FK allows access to employee model through department serializer'''
    department = models.ForeignKey("Department", on_delete=models.CASCADE, related_name="roster")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Training(models.Model):
    name = models.CharField(default="", max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    max_attendees = models.IntegerField()
    employees = models.ManyToManyField("Employee", through='EmployeeTraining')

    def __str__(self):
        return self.name

class EmployeeTraining(models.Model):
    '''Join Table showing employee's participation in a training program'''
    employee = models.ForeignKey("Employee", on_delete=models.CASCADE)
    training = models.ForeignKey("Training", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.employee.first_name}  {self.employee.last_name} is scheduled for {self.training.name}"

class Computer(models.Model):
    """A device that is assigned to a company employee"""

    purchase_date = models.DateField('Purchase Date')
    decommission_date = models.DateField('Decommission Date', default=None, blank=True, null=True)
    manufacturer = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    employee = models.ManyToManyField(Employee, through='ComputerEmployee')

    def __str__(self):
        computer_name = (f"{self.manufacturer} {self.model} - ID#{self.id}")
        return computer_name

class ComputerEmployee(models.Model):
    """a relationship between computers and employees"""
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT)
    computer = models.ForeignKey('Computer', on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} is assigned to {self.computer.id}"