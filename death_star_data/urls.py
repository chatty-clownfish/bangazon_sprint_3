from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from death_star_data import views

router = DefaultRouter()
router.register('training', views.TrainingViewSet)

urlpatterns = [
    path('', include(router.urls))
]

