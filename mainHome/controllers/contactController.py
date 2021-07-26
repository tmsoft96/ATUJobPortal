from ATUJobPortal.config.auth import Auth
from django.shortcuts import render


def contactUsController(request):
    auth = Auth(request)
    return render(request, 'contact.html',
                  {'heading': 'Contact',
                   "auth": auth.authMap})
