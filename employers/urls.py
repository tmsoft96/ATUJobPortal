from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.employerRegisterForm, name="employerRegisterForm"),
]
