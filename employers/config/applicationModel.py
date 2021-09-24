from ATUJobPortal.config.firebase import Firebase
import timeago
import datetime


class ApplicationModel:
    def __init__(self) -> None:
        pass

    def paticularApplication(jobId, customerId):
        firebase = Firebase()

        now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)
        application = firebase.db.child("Application").child(
            jobId).child(customerId).get().val().items()
        jobDictConvert = dict(application)

        createdDate = datetime.datetime.fromisoformat(
            jobDictConvert.get("createdDate"))

        applicationDict = {
            "jobId": jobDictConvert.get("jobId"),
            "customerId":jobDictConvert.get("customerId"),
            "companyId": jobDictConvert.get("companyId"),
            "fname": jobDictConvert.get("fname"),
            "lname": jobDictConvert.get("lname"),
            "phone": jobDictConvert.get("phone"),
            "qualification": jobDictConvert.get("qualification"),
            "yearExperience": jobDictConvert.get("yearExperience"),
            "note": jobDictConvert.get("note"),
            "cv": jobDictConvert.get("cv"),
            "status": jobDictConvert.get("status"),
            "time": timeago.format(createdDate, now),
        }

        return applicationDict
