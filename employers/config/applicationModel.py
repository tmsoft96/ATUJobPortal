from ATUJobPortal.config.constant import Constants
from customer.config.userModel import CustomerUserModel
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
            applications = firebase.db.child("Application").child(
                companyId).get().val().items()

            now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)

            for key, value in applications:
                editDate = datetime.datetime.fromisoformat(
                    value.get("editDate"))
                customerId = value.get("customerId")
                profilePicture = firebase.db.child("Users").child(
                    customerId).child("profilePicture").get().val()
                applicationDict = {
                    "jobId": value.get("jobId"),
                    "customerId": customerId,
                    "companyId": value.get("companyId"),
                    "fname": value.get("fname"),
                    "lname": value.get("lname"),
                    "phone": value.get("phone"),
                    "profilePicture": profilePicture,
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
        constants = Constants()

        now = datetime.datetime.now() + datetime.timedelta(seconds=60 * 3.4)
        application = firebase.db.child("Application").child(
            companyId).child(jobId).get().val().items()
        applicationConvert = dict(application)

        editDate = datetime.datetime.fromisoformat(
            applicationConvert.get("editDate"))

        customerId = applicationConvert.get("customerId")
        customerDict = CustomerUserModel.userModel(customerId)

        # check for status to fetch appointment detials
        status = applicationConvert.get("status")
        appointmentDict = {}
        if status == constants.jobstatus[2] or status == constants.jobstatus[3]:
            appointment = firebase.db.child("Appointments").child(
                companyId).child(customerId).get().val().items()
            appointmentConvert = dict(appointment)
            appointmentEditDate = datetime.datetime.fromisoformat(
            appointmentConvert.get("editDate"))
            appointmentDict = {
                "status": appointmentConvert.get("status"),
                "note": appointmentConvert.get("note"),
                "jobId": appointmentConvert.get("jobId"),
                "date": appointmentConvert.get("date"),
                "time": appointmentConvert.get("time"),
                "venue": appointmentConvert.get("venue"),
                "customerId": appointmentConvert.get("customerId"),
                "editDate": timeago.format(appointmentEditDate, now),
            }

        applicationDict = {
            "jobId": applicationConvert.get("jobId"),
            "customerId": customerId,
            "companyId": applicationConvert.get("companyId"),
            "fname": applicationConvert.get("fname"),
            "lname": applicationConvert.get("lname"),
            "phone": applicationConvert.get("phone"),
            "email": customerDict.get("email"),
            "dob": customerDict.get("dob"),
            "professionalHeadline": customerDict.get("professionalHeadline"),
            "gender": "Male" if customerDict.get("gender") == "M" else "Female",
            "nationality": customerDict.get("nationality"),
            "location": customerDict.get("location"),
            "profilePicture": customerDict.get("profilePicture"),
            "qualification": applicationConvert.get("qualification"),
            "yearExperience": applicationConvert.get("yearExperience"),
            "note": applicationConvert.get("note"),
            "cv": applicationConvert.get("cv"),
            "status": status,
            "time": timeago.format(editDate, now),
            "appointment": appointmentDict if status == constants.jobstatus[2] or status == constants.jobstatus[3] else None,
        }

        return applicationDict
