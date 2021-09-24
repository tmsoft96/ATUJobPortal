from employers.config.jobModel import JobModel
from employers.config.userModel import EmployerUserModel
from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.firebase import Firebase
from ATUJobPortal.config.dictionary import Dictionary
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render
from datetime import datetime


def employerPostJobController(request):
    auth = Authentication(request)
    dictionary = Dictionary()
    firebase = Firebase()

    yearExperienceList = []

    for yearEx in range(1, 6):
        yearExperienceList.append(yearEx)

    userDetails = None
    if auth.authMap["authorize"]:
        userId = auth.authMap["userId"]
        userDetails = EmployerUserModel.userModel(userId)
        print(userDetails)
    else:
        return HttpResponseRedirect("/account/logout")

    if request.method == "GET":
        if request.GET.get("action") == "edit":
            key = request.GET.get("key")
            jobDict = JobModel.particularJob(key)
            print(jobDict)
            return render(request,
                          'employerPostJobEdit.html',
                          {"heading": "Post A Job | ATU Job Portal",
                           "industries": dictionary.industriesList,
                           "jobFunctions": dictionary.currentJobsFunctionList,
                           "workTypes": dictionary.workTypeList,
                           "regions": dictionary.regionList,
                           "yearExperiences": yearExperienceList,
                           "qualifications": dictionary.qualificationsList,
                           "jobLevels": dictionary.jobLevelList,
                           "currencies": dictionary.currencyList,
                           "salaries": dictionary.salaryList,
                           'auth': auth.authMap,
                           "userDetails": userDetails,
                           "jobDict": jobDict,
                           "key": key})

    if request.method == "POST":
        if request.POST.get("button") == "postJob":
            job = {
                "companyId": userDetails.get("id"),
                "companyName": userDetails.get("companyName"),
                "companyWebsite": userDetails.get("website"),
                "companyEmail": userDetails.get("email"),
                "companyLogo":  userDetails.get("logo"),
                "jobTitle": request.POST.get("jobTitle"),
                "jobFunction": request.POST.get("jobFunction"),
                "industry": request.POST.get("industry"),
                "workType": request.POST.get("workType"),
                "region": request.POST.get("region"),
                "qualification": request.POST.get("qualification"),
                "yearExperience": request.POST.get("yearExperience"),
                "jobLevel": request.POST.get("jobLevel"),
                "negotiable": True if request.POST.get("negotiable") == "on" else False,
                "currency": request.POST.get("currency"),
                "salary": request.POST.get("salary"),
                "plusCommission": True if request.POST.get("plusCommission") == "on" else False,
                "availableOpenings": request.POST.get("availableOpenings"),
                "jobSummary": request.POST.get("jobSummary"),
                "jobDescription": request.POST.get("jobDescription"),
                "applyWith": "applyWithCoverLetter" if request.POST.get("applyWithCoverLetter") == "on" else "applyWithCoverLetterOrNot",
                "viewBy": "viewByPortalAndEmail" if request.POST.get("viewByPortalAndEmail") == "on" else "viewByPortal",
                "timestamp": datetime.now().timestamp(),
                "createdDate": str(datetime.now()),
                "editDate": str(datetime.now()),
                "delete": False,
            }
            firebase.db.child("Jobs").push(job)

            # adding no of add job to user profile
            noOfJobs = userDetails.get("noOfJobs")
            firebase.db.child("Users").child(
                userId).update({"noOfJobs": noOfJobs + 1})

            return HttpResponseRedirect("/employer/dashboard?action=jobSuccess")

        elif request.POST.get("button") == "editJob":
            key = request.POST.get("key")
            job = {
                "jobTitle": request.POST.get("jobTitle"),
                "jobFunction": request.POST.get("jobFunction"),
                "industry": request.POST.get("industry"),
                "workType": request.POST.get("workType"),
                "region": request.POST.get("region"),
                "qualification": request.POST.get("qualification"),
                "yearExperience": request.POST.get("yearExperience"),
                "jobLevel": request.POST.get("jobLevel"),
                "negotiable": True if request.POST.get("negotiable") == "on" else False,
                "currency": request.POST.get("currency"),
                "salary": request.POST.get("salary"),
                "plusCommission": True if request.POST.get("plusCommission") == "on" else False,
                "availableOpenings": request.POST.get("availableOpenings"),
                "jobSummary": request.POST.get("jobSummary"),
                "jobDescription": request.POST.get("jobDescription"),
                "timestamp": datetime.now().timestamp(),
                "editDate": str(datetime.now()),
            }
            firebase.db.child("Jobs").child(key).update(job)

            return HttpResponseRedirect("/employer/dashboard?action=jobEditSuccess")

    return render(request,
                  'employerPostJob.html',
                  {"heading": "Post A Job | ATU Job Portal",
                   "industries": dictionary.industriesList,
                   "jobFunctions": dictionary.currentJobsFunctionList,
                   "workTypes": dictionary.workTypeList,
                   "regions": dictionary.regionList,
                   "yearExperiences": yearExperienceList,
                   "qualifications": dictionary.qualificationsList,
                   "jobLevels": dictionary.jobLevelList,
                   "currencies": dictionary.currencyList,
                   "salaries": dictionary.salaryList,
                   'auth': auth.authMap,
                   "userDetails": userDetails})
