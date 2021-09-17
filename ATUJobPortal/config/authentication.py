class Authentication:
    authMap = {
        "authorize": False,
        "userType": None,
        "userId": None,
        "idToken": None,
        "verifyEmail": False,
    }

    def __init__(self, request):
        if (request is not None):
            try:
                if (request.session["authorize"]):
                    self.authMap["authorize"] = True
                    self.authMap["userType"] = request.session["userType"]
                    self.authMap["userId"] = request.session["userId"]
                    self.authMap["idToken"] = request.session["idToken"]
                    self.authMap["verifyEmail"] = request.session["verifyEmail"]
                else:
                    self.authMap["authorize"] = False
                    self.authMap["userType"] = None
                    self.authMap["userId"] = None
                    self.authMap["idToken"] = None
                    self.authMap["verifyEmail"] = False
            except: 
                self.authMap["authorize"] = False
                self.authMap["userType"] = None
                self.authMap["userId"] = None
                self.authMap["idToken"] = None
                self.authMap["verifyEmail"] = False
