from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def contactUsController(request):
    auth = Authentication(request)
    return render(request, 'contact.html',
                  {'heading': 'Contact',
                   "auth": auth.authMap})
