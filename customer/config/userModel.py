from ATUJobPortal.config.firebase import Firebase


class CustomerUserModel:
    def __init__(self) -> None:
        pass

    def userModel(userId):
        firebase = Firebase()
        user = firebase.db.child("Users").child(userId).get().val()
        userDictConvert = dict(user)
        
        userDetail = {
            "id": userId,
            "userType":userDictConvert.get("userType"),
            "lname":userDictConvert.get("lname"),
            "fname":userDictConvert.get("fname"),
            "gender":userDictConvert.get("gender"),
            "email":userDictConvert.get("email"),
            "dob":userDictConvert.get("dob"),
            "nationality":userDictConvert.get("nationality"),
            "location":userDictConvert.get("location"),
            "phone":userDictConvert.get("phone"),
            "qualification":userDictConvert.get("qualification"),
            "currentJobFunction":userDictConvert.get("currentJobFunction"),
            "yearExperience":userDictConvert.get("yearExperience"),
            "cv":userDictConvert.get("cv"),
            "profilePicture":userDictConvert.get("profilePicture"),
            "professionalHeadline":userDictConvert.get("professionalHeadline"),
            "preferredJobFunction":userDictConvert.get("preferredJobFunction"),
            "workType":userDictConvert.get("workType"),
            "salaryExpectation":userDictConvert.get("salaryExpectation"),
            "tipsAlert":userDictConvert.get("tipsAlert"),
            "jobAlerts":userDictConvert.get("jobAlerts"),
            "note":userDictConvert.get("note"),
        }
        return userDetail
