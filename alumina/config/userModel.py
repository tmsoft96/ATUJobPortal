from employers.config.jobModel import JobModel
from employers.config.applicationModel import ApplicationModel
from ATUJobPortal.config.constant import Constants
from ATUJobPortal.config.firebase import Firebase


class AluminaUserModel:
    def __init__(self) -> None:
        pass

    def userModel(userId):
        firebase = Firebase()
        constants = Constants()

        user = firebase.db.child("Users").child(userId).get().val()
        userDictConvert = dict(user)

        noOfApplications = 0
        noOfJobs = 0
        noOfCustomers = 0
        noOfEmployers = 0

        allApplicationsList = []
        jobList = []

        # getting all applications
        applications = firebase.db.child("Application").get().val().items()
        for companyId, value in applications:
            for key in value:
                noOfApplications += 1
                allApplicationsList = ApplicationModel.allCompanyApplication(companyId)

        # getting all jobs
        jobs = firebase.db.child("Jobs").get().val().items()
        for jobKey, value in jobs:
            noOfJobs += 1
            jobList = JobModel.allJob()

        # getting all users
        users = firebase.db.child("Users").get().val().items()
        for userKey, value in users:
            if value.get("userType") == constants.userType[0]:
                noOfCustomers += 1
            elif value.get("userType") == constants.userType[1]:
                noOfEmployers += 1


        userDetail = {
            "id": userId,
            "userType": userDictConvert.get("userType"),
            "lname": userDictConvert.get("lname"),
            "fname": userDictConvert.get("fname"),
            "gender": userDictConvert.get("gender"),
            "email": userDictConvert.get("email"),
            "dob": userDictConvert.get("dob"),
            "phone": userDictConvert.get("phone"),
            "cv": userDictConvert.get("cv"),
            "profilePicture": userDictConvert.get("profilePicture"),
            "permission": userDictConvert.get("permission"),
            "noOfApplications": noOfApplications,
            "noOfJobs": noOfJobs,
            "noOfCustomers": noOfCustomers,
            "noOfEmployers": noOfEmployers,
            "allApplicationsList": allApplicationsList,
            "jobList": jobList,
        }
        return userDetail
