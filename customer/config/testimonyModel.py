from typing import Dict
from ATUJobPortal.config.firebase import Firebase


class TestimonyModel:
    def __init__(self) -> None:
        pass

    def allTestimony():
        firebase = Firebase()

        testimonyList = []
        allTestimony = firebase.db.child("Testimony").get().val().items()

        for key, value in allTestimony:
            testimonyDict = {
                "testimony": value.get("testimony"),
                "id": value.get("id"),
                "name": value.get("name"),
                "profilePicture": value.get("profilePicture"),
            }
            testimonyList.append(testimonyDict)
        
        return testimonyList