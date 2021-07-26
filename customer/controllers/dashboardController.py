from ATUJobPortal.config.auth import Auth
from django.shortcuts import render


def dashboardController(request):
    auth = Auth(request)
    return render(request,
                  'customerDashboard.html',
                  {"heading": "Job Seeker Profile | ATU Job Portal",
                   "auth": auth.authMap})
