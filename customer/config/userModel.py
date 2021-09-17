from ATUJobPortal.config.firebase import Firebase


class CustomerUserModel:
    def __init__(self) -> None:
        pass

    def userModel(userId):
        userDetail = {
            "id": userId,
            "userType": getData(userId, "userType"),
            "lname": getData(userId, "lname"),
            "fname": getData(userId, "fname"),
            "gender": getData(userId, "gender"),
            "email": getData(userId, "email"),
            "dob": getData(userId, "dob"),
            "nationality": getData(userId, "nationality"),
            "location": getData(userId, "location"),
            "phone": getData(userId, "phone"),
            "qualification": getData(userId, "qualification"),
            "currentJobFunction": getData(userId, "currentJobFunction"),
            "yearExperience": getData(userId, "yearExperience"),
            "cv": getData(userId, "cv"),
            "profilePicture": getData(userId, "profilePicture"),
            "professionalHeadline": getData(userId, "professionalHeadline"),
            "preferredJobFunction": getData(userId, "preferredJobFunction"),
            "workType": getData(userId, "workType"),
            "salaryExpectation": getData(userId, "salaryExpectation"),
            "tipsAlert": getData(userId, "tipsAlert"),
            "jobAlerts": getData(userId, "jobAlerts"),
        }
        return userDetail


def getData(userId, key):
    firebase = Firebase()
    return firebase.db.child("Users").child(userId).child(key).get().val()
