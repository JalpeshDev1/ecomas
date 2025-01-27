class SystemException(Exception):
    def __init__(self,status_code,message):
        self.status_code=status_code
        self.message = message
        super().__init__(self.message)

class UserDoseNotExists(Exception):
    def __init__(self,status_code):
        self.status_code=status_code
        self.message = "User Dose Not Exists"
        super().__init__(self.message)

class FileNotSupported(Exception):
    def __init__(self,status_code):
        self.status_code=status_code
        self.message = "File not supported. Please try a different PDF"
        super().__init__(self.message)

