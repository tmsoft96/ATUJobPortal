from employers.config.jobModel import JobModel
from ATUJobPortal.config.constant import Constants
from customer.config.userModel import CustomerUserModel
from employers.config.userModel import EmployerUserModel
from django.shortcuts import render
from ATUJobPortal.config.authentication import Authentication


def indexController(request):
    auth = Authentication(request)
    constants = Constants()
    jobs = JobModel.allJob()

    userDetails = None

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(
            userId) if auth.authMap["userType"] == constants.userType[1] else CustomerUserModel.userModel(userId)
        print(userDetails)

    return render(request, 'index.html',
                  {'heading': 'Home',
                   "auth": auth.authMap,
                   "userDetails": userDetails,
                   "jobs": jobs if len(jobs) <= 7 else jobs[:7]})
