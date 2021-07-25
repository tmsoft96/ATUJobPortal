from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.customerRegisterForm, name="customerRegisterForm"),
]
