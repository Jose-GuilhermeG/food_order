class ValidationException(Exception):
    def __init__(self, message : str = "validation err" , field = ""):
        super().__init__(message)
        self.message_err = f"{field} err : {message}"

    def __str__(self):
        return self.message_err

class IdValidationException(ValidationException):
    def __init__(self, message = "id validation err", field="id"):
        super().__init__(message, field)

class EmptyValidationException(ValidationException):
    def __init__(self, message = "this field can't be empty", field=""):
        super().__init__(message, field)

class IntegrityException(Exception):
    def __init__(self, message : str = "bad request" , code : int = 400):
        super().__init__(message)
        self.code = code
        self.message = message

class InternalException(Exception):
    def __init__(self, message = ""):
        super().__init__(message)
