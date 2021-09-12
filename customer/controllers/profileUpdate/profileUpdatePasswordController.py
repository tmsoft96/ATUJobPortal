from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def profileUpdatePasswordController(request):
    auth = Authentication(request)

    return render(request,
                  'customerProfileUpdate_password.html',
                  {"heading": "Account Settings| ATU Job Portal",
                   "auth": auth.authMap})