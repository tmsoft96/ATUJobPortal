from django.urls import path
from . import views

urlpatterns = [
    path('sign-up', views.signUp, name="customerSignUp"),
    path('dashboard', views.dashboard, name="customerDashboard"),
    path('profile', views.careerProfile, name="careerProfile"),
    path('profile/employment', views.careerProfileEmployment, name="profileEmployment"),
]
