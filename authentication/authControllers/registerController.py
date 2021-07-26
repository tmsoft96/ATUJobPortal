from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def registerController(request):
    auth = Authentication(request)
    return render(request, 'register.html',
                  {"heading": "register",
                   'auth': auth.authMap})
