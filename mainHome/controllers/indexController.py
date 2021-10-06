from customer.config.testimonyModel import TestimonyModel
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
    testimonies = TestimonyModel.allTestimony()

    userDetails = None
    regions = []

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(
            userId) if auth.authMap["userType"] == constants.userType[1] else CustomerUserModel.userModel(userId)
        print(userDetails)

    for job in jobs:
        if not job.get("delete"):
            try:
                regions.index(job.get("region")) 
            except ValueError:
                regions.append(job.get("region"))

    regions.sort()


    return render(request, 'index.html',
                  {'heading': 'Home',
                   "auth": auth.authMap,
                   "userDetails": userDetails,
                   "jobs": jobs if len(jobs) <= 7 else jobs[:7],
                   "regions": regions,
                   "testimonies": testimonies})
