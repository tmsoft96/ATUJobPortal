from django.core.files.storage import FileSystemStorage
import time
from ATUJobPortal.config.authentication import Authentication
from ATUJobPortal.config.firebase import Firebase


def uploadFile(request, file, pathName):
    firebase = Firebase()
    fs = FileSystemStorage()
    auth = Authentication(request)

    idToken = auth.authMap["idToken"]

    fs.save(file.name, file)
    timestamp = time.time()
    firebase.storage.child(
        pathName + "/" + str(timestamp)).put("media/" + file.name)
    url = firebase.storage.child(
        pathName + "/" + str(timestamp)).get_url(idToken)
    print(url)
    fs.delete(file.name)
    return url
