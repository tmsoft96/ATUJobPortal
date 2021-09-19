from django.http.response import HttpResponseRedirect
from ATUJobPortal.config.firebase import Firebase
from ATUJobPortal.config.dictionary import Dictionary
from ATUJobPortal.config.authentication import Authentication
from django.shortcuts import render

def employerPostJobController(request):
    auth = Authentication(request)
    dictionary = Dictionary()
    firebase = Firebase()

    yearExperienceList = []

    for yearEx in range(1, 6):
        yearExperienceList.append(yearEx)

    if request.method == "POST":
        if request.POST.get("button") == "postJob":
            job = {
                "companyId": "",
                "jobTitle": request.POST.get("jobTitle"),
                "jobFunction": request.POST.get("jobFunction"),
                "industry": request.POST.get("industry"),
                "workType": request.POST.get("workType"),
                "region": request.POST.get("region"),
                "qualification": request.POST.get("qualification"),
                "yearExperience": request.POST.get("yearExperience"),
                "negotiable": request.POST.get("negotiable"),
                "salary": request.POST.get("salary"),
                "plusCommission": request.POST.get("plusCommission"),
                "availableOpenings": request.POST.get("availableOpenings"),
                "jobSummary": request.POST.get("jobSummary"),
                "jobDescription": request.POST.get("jobDescription"),
                "applyWith": "applyWithCoverLetter" if request.POST.get("applyWithCoverLetter") == "on" else "applyWithCoverLetterOrNot" ,
                "viewBy": "viewByPortalAndEmail" if request.POST.get("viewByPortalAndEmail") == "on" else "viewByPortal" ,
            }
            firebase.db.child("Jobs").push(job)

            return HttpResponseRedirect("/employer/dashboard?action=jobSuccess") 

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
                   'auth': auth.authMap})