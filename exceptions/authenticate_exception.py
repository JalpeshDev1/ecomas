class EmailNotRegistered(Exception):
    def __init__(self,status_code):
        self.status_code=status_code
        self.message = "Email is not registered"
        super().__init__(self.message)

class WrongPassword(Exception):
    def __init__(self,status_code):
        self.status_code=status_code
        self.message = "Password is wrong"
        super().__init__(self.message)

class EmailAlreadyExists(Exception):
    def __init__(self,status_code):
        self.status_code=status_code
        self.message = "Email already exists"
        super().__init__(self.message)

class PasswordDoseNotMatch(Exception):
    def __init__(self,status_code):
        self.status_code=status_code
        self.message = "New Password and Confirm Password dosen't match"
        super().__init__(self.message)

class InvalidResetLink(Exception):
    def __init__(self,status_code):
        self.status_code=status_code
        self.message = "Invalid Reset Link"
        super().__init__(self.message)

class ExpiredToken(Exception):
    def __init__(self,status_code):
        self.status_code=status_code
        self.message = "Link is expired"
        super().__init__(self.message)

class InvalidEmailDomain(Exception):
    def __init__(self,status_code):
        self.status_code=status_code
        self.message = "Not a Valid Email"
        super().__init__(self.message)