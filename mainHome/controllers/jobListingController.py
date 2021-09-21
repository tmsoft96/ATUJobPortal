from customer.config.userModel import CustomerUserModel
from employers.config.userModel import EmployerUserModel
from employers.config.jobModel import JobModel
from ATUJobPortal.config.constant import Constants
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render


def jobListingController(request):
    auth = Authentication(request)
    constants = Constants()
    jobs = JobModel.allJob()

    userDetails = None
    workTypes = []
    regions = []
    yearExperiences = []

    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(
            userId) if auth.authMap["userType"] == constants.userType[1] else CustomerUserModel.userModel(userId)
        print(userDetails)

    for job in jobs:
        if not job.get("delete"):
            try:
                workTypes.index(job.get("workType")) 
            except ValueError:
                workTypes.append(job.get("workType"))
            
            try:
                regions.index(job.get("region")) 
            except ValueError:
                regions.append(job.get("region"))

            try:
                yearExperiences.index(job.get("yearExperience")) 
            except ValueError:
                yearExperiences.append(job.get("yearExperience"))

    workTypes.sort()
    regions.sort()
    yearExperiences.sort()
    totalJobs = len(jobs)
    return render(request, 'jobListing.html',
                  {'heading': "Job Listing",
                   "auth": auth.authMap,
                   "userDetails": userDetails,
                   "jobs": jobs,
                   "workTypes": workTypes,
                   "regions": regions,
                   "yearExperiences": yearExperiences,
                   "totalJobs": totalJobs})
