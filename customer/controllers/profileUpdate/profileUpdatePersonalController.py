from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def profileUpdatePersonalController(request):
    auth = Authentication(request)

    return render(request,
                  'customerProfileUpdate_personal.html',
                  {"heading": "Account Settings| ATU Job Portal",
                   "auth": auth.authMap})