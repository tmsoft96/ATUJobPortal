from ATUJobPortal.config.firebase import Firebase
import timeago
import datetime


class ApplicationModel:
    def __init__(self) -> None:
        pass

    def allCompanyApplication(companyId):
        firebase = Firebase()

        applicationList = []
        try:
            applications = firebase.db.child("Application").child(companyId).get().val().items()

            now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)

            for key, value in applications:
                editDate = datetime.datetime.fromisoformat(
                value.get("editDate"))
                applicationDict = {
                    "jobId": value.get("jobId"),
                    "customerId":value.get("customerId"),
                    "companyId": value.get("companyId"),
                    "fname": value.get("fname"),
                    "lname": value.get("lname"),
                    "phone": value.get("phone"),
                    "profilePicture": value.get("profilePicture"),
                    "qualification": value.get("qualification"),
                    "yearExperience": value.get("yearExperience"),
                    "status": value.get("status"),
                    "time": timeago.format(editDate, now),
                }
                applicationList.append(applicationDict)
        except:
            print("No job application")

        return applicationList


    def paticularApplication(companyId, jobId):
        firebase = Firebase()

        now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)
        application = firebase.db.child("Application").child(
            companyId).child(jobId).get().val().items()
        applicationConvert = dict(application)

        editDate = datetime.datetime.fromisoformat(
            applicationConvert.get("editDate"))

        applicationDict = {
            "jobId": applicationConvert.get("jobId"),
            "customerId":applicationConvert.get("customerId"),
            "companyId": applicationConvert.get("companyId"),
            "fname": applicationConvert.get("fname"),
            "lname": applicationConvert.get("lname"),
            "phone": applicationConvert.get("phone"),
            "profilePicture": applicationConvert.get("profilePicture"),
            "qualification": applicationConvert.get("qualification"),
            "yearExperience": applicationConvert.get("yearExperience"),
            "note": applicationConvert.get("note"),
            "cv": applicationConvert.get("cv"),
            "status": applicationConvert.get("status"),
            "time": timeago.format(editDate, now),
        }

        return applicationDict
