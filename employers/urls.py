from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.signUp, name="employerSignUp"),
    path('dashboard', views.dashboard, name="employerDashboard"),
]
