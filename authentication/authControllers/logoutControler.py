from django.shortcuts import render

def logoutController(request):
    return render(request, 'login.html', {"heading": "login"})