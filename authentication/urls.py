from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('customer/sign-up', views.studentRegisterForm,
         name="studentRegisterForm"),
]
