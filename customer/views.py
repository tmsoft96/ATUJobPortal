from customer.controllers.studentRegisterFormController import customerRegisterFormController
from django.shortcuts import render

def customerRegisterForm(request):
    return customerRegisterFormController(request)