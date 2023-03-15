from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("", BusinessCreateViewSet, basename="create_business")

urlpatterns = [
    path("", include(router.urls)),
    path('id/<int:pk>/', getbusiness, name='business'),
    path('category/<str:category>/', getcategory, name="category"),
]