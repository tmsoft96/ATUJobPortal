from ATUJobPortal.config.firebase import Firebase


class EmployerUserModel:
    def __init__(self) -> None:
        pass

    def userModel(userId):
        firebase = Firebase()
        user = firebase.db.child("Users").child(userId).get().val()
        userDictConvert = dict(user)

        userDetail = {
            "id": userId,
            "userType": userDictConvert.get("userType"),
            "lname": userDictConvert.get("lname"),
            "fname": userDictConvert.get("fname"),
            "email": userDictConvert.get("email"),
            "position": userDictConvert.get("position"),
            "phone" : userDictConvert.get("phone"),
            "companyName": userDictConvert.get("companyName"),
            "industry": userDictConvert.get("industry"),
            "employeesNumber": userDictConvert.get("employeesNumber"),
            "employerType": userDictConvert.get("employerType"),
            "website": userDictConvert.get("website"),
            "address": userDictConvert.get("address"),
            "noOfJobs": userDictConvert.get("noOfJobs"),
            "noOfApplication": userDictConvert.get("noOfApplication"),
            "noOfViews": userDictConvert.get("noOfViews"),
            "logo": userDictConvert.get("logo"),
        }
        return userDetail

