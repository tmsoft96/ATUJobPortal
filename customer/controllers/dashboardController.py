from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def dashboardController(request):
    auth = Authentication(request)
    return render(request,
                  'customerDashboard.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal",
                   "auth": auth.authMap})
