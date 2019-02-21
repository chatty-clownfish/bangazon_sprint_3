from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from death_star_data import views

router = DefaultRouter()
router.register('department', views.DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls))
]

