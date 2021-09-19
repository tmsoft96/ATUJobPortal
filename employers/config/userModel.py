from ATUJobPortal.config.firebase import Firebase


class EmployerUserModel:
    def __init__(self) -> None:
        pass

    def userModel(userId):
        userDetail = {
            "id": userId,
            "userType": getData(userId, "userType"),
            "lname": getData(userId, "lname"),
            "fname": getData(userId, "fname"),
            "email": getData(userId, "email"),
            "position": getData(userId, "position"),
            "phone" : getData(userId, "phone"),
            "companyName": getData(userId, "companyName"),
            "industry": getData(userId, "industry"),
            "employeesNumber": getData(userId, "employeesNumber"),
            "employerType": getData(userId, "employerType"),
            "website": getData(userId, "website"),
            "address": getData(userId, "address"),
            "noOfJobs": getData(userId, "noOfJobs"),
            "noOfApplication": getData(userId, "noOfApplication"),
            "noOfViews": getData(userId, "noOfViews"),
        }
        return userDetail


def getData(userId, key):
    firebase = Firebase()
    return firebase.db.child("Users").child(userId).child(key).get().val()
