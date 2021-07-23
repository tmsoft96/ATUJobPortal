from django.shortcuts import render


def loginController(request):
    return render(request, 'login.html', {"heading": "login"})
