from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def profileUpdatePhoneController(request):
    auth = Authentication(request)

    return render(request,
                  'customerProfileUpdate_phone.html',
                  {"heading": "Account Settings| ATU Job Portal",
                   "auth": auth.authMap})