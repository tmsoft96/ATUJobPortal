class Authentication:
    authMap = {
        "authorize": False,
        "userType": None,
    }

    def __init__(self, request):
        if (request is not None):
            try:
                if (request.session["authorize"]):
                    self.authMap["authorize"] = True
                    self.authMap["userType"] = request.session["userType"]
            except: 
                self.authMap["authorize"] = False
                self.authMap["userType"] = None
