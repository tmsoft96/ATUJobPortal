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
        }
        return userDetail


def getData(userId, key):
    firebase = Firebase()
    return firebase.db.child("Users").child(userId).child(key).get().val()
