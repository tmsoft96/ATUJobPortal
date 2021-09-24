from ATUJobPortal.config.constant import Constants
from ATUJobPortal.config.firebase import Firebase
import timeago
import datetime


class CustomerUserModel:
    def __init__(self) -> None:
        pass

    def userModel(userId):
        firebase = Firebase()
        constants = Constants()

        now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)

        user = firebase.db.child("Users").child(userId).get().val()
        userDictConvert = dict(user)

        appliedJobList = []
        oneAppliedJob = None

        try:
            appliedJob = userDictConvert.get("appliedJob").values()
            for value in appliedJob:
                createdDate = datetime.datetime.fromisoformat(
                    value.get("createdDate"))
                companyId = value.get("companyId")
                jobId = value.get("jobId")
                status = value.get("status")

                job = firebase.db.child("Jobs").child(jobId).get().val()
                jobDictConvert = dict(job)
                appliedJobList.append({
                    "companyId": companyId,
                    "jobId": jobId,
                    "logo": jobDictConvert.get("companyLogo"),
                    "companyName": jobDictConvert.get("companyName"),
                    "jobTitle": jobDictConvert.get("jobTitle"),
                    "jobFunction": jobDictConvert.get("jobFunction"),
                    "region": jobDictConvert.get("region"),
                    "currency": jobDictConvert.get("currency"),
                    "salary": jobDictConvert.get("salary"),
                    "status": status,
                    "time": timeago.format(createdDate, now),
                })
        except:
            pass

        # load only one pending job application
        for value in appliedJobList:
            if value.get("status") == constants.jobstatus[0]:
                oneAppliedJob = value
                break

        userDetail = {
            "id": userId,
            "userType": userDictConvert.get("userType"),
            "lname": userDictConvert.get("lname"),
            "fname": userDictConvert.get("fname"),
            "gender": userDictConvert.get("gender"),
            "email": userDictConvert.get("email"),
            "dob": userDictConvert.get("dob"),
            "nationality": userDictConvert.get("nationality"),
            "location": userDictConvert.get("location"),
            "phone": userDictConvert.get("phone"),
            "qualification": userDictConvert.get("qualification"),
            "currentJobFunction": userDictConvert.get("currentJobFunction"),
            "yearExperience": userDictConvert.get("yearExperience"),
            "cv": userDictConvert.get("cv"),
            "profilePicture": userDictConvert.get("profilePicture"),
            "professionalHeadline": userDictConvert.get("professionalHeadline"),
            "preferredJobFunction": userDictConvert.get("preferredJobFunction"),
            "workType": userDictConvert.get("workType"),
            "salaryExpectation": userDictConvert.get("salaryExpectation"),
            "tipsAlert": userDictConvert.get("tipsAlert"),
            "jobAlerts": userDictConvert.get("jobAlerts"),
            "note": userDictConvert.get("note"),
            "appliedJobList": appliedJobList,
            "oneAppliedJob": oneAppliedJob,
        }
        return userDetail
