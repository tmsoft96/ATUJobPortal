from customer.controllers.signUpController import signUpController
from django.shortcuts import render

def signUp(request):
    return signUpController(request)