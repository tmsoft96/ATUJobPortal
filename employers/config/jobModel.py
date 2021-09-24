from ATUJobPortal.config.firebase import Firebase
import timeago
import datetime


class JobModel:
    def __init__(self) -> None:
        pass

    def allJob():
        firebase = Firebase()

        now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)

        allJobsList = []
        allJobs = firebase.db.child("Jobs").get().val().items()

        for key, value in allJobs:
            postDate = datetime.datetime.fromisoformat(value.get("editDate"))
            jobDic = {
                "key": key,
                "jobTitle": value.get("jobTitle"),
                "jobFunction": value.get("jobFunction"),
                "region": value.get("region"),
                "currency": value.get("currency"),
                "salary": value.get("salary"),
                "workType": value.get("workType"),
                "delete": value.get("delete"),
                "time": timeago.format(postDate, now),
                "companyId": value.get("companyId"),
                "companyName": value.get("companyName"),
                "companyLogo": value.get("companyLogo"),
                "yearExperience": value.get("yearExperience"),
            }
            allJobsList.append(jobDic)

        return allJobsList

    def particularJob(key):
        firebase = Firebase()

        now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)
        job = firebase.db.child("Jobs").child(key).get().val().items()
        jobDictConvert = dict(job)

        postDate = datetime.datetime.fromisoformat(jobDictConvert.get("editDate"))
        jobDict = {
            "companyId": jobDictConvert.get("companyId"),
            "companyName": jobDictConvert.get("companyName"),
            "companyWebsite": jobDictConvert.get("companyWebsite"),
            "companyEmail": jobDictConvert.get("companyEmail"),
            "companyLogo": jobDictConvert.get("companyLogo"),
            "jobTitle": jobDictConvert.get("jobTitle"),
            "jobFunction": jobDictConvert.get("jobFunction"),
            "industry": jobDictConvert.get("industry"),
            "workType": jobDictConvert.get("workType"),
            "region": jobDictConvert.get("region"),
            "qualification": jobDictConvert.get("qualification"),
            "yearExperience": jobDictConvert.get("yearExperience"),
            "negotiable": jobDictConvert.get("negotiable"),
            "currency": jobDictConvert.get("currency"),
            "salary": jobDictConvert.get("salary"),
            "plusCommission": jobDictConvert.get("plusCommission"),
            "availableOpenings": jobDictConvert.get("availableOpenings"),
            "jobSummary": jobDictConvert.get("jobSummary"),
            "jobLevel": jobDictConvert.get("jobLevel"),
            "jobDescription": jobDictConvert.get("jobDescription"),
            "applyWith": jobDictConvert.get("applyWith"),
            "viewBy": jobDictConvert.get("viewBy"),
            "timestamp": jobDictConvert.get("timestamp"),
            "createdDate": jobDictConvert.get("createdDate"),
            "editDate": str(jobDictConvert.get("editDate")).split(" ")[0],
            "delete": jobDictConvert.get("delete"),
            "time": timeago.format(postDate, now),
        }
        return jobDict
