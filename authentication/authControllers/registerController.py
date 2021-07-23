from django.shortcuts import render

def registerController(request):
    return render(request, 'register.html', {"heading": "register"})