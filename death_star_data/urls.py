from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from death_star_data import views


router = DefaultRouter()
router.register('department', views.DepartmentViewSet)
router.register('employee', views.EmployeeViewSet)
router.register('producttype', views.ProductTypeViewSet)
router.register('paymenttype', views.PaymentTypeViewSet)
router.register('customer', views.CustomerViewSet)
router.register('product', views.ProductViewSet)
router.register('order', views.OrderViewSet)
router.register('training', views.TrainingViewSet)
router.register('computer', views.ComputerViewSet)


urlpatterns = [
    path('', include(router.urls))
]

