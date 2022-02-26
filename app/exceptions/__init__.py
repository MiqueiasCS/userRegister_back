class InvalidValueError(Exception):
    data_types = {
    str:"string",
    int:"integer",
    float:"float",
    list:"list",
    bool:"boolean"
}

    def __init__(self,received_data:dict,expected:dict):
        self.message = {
            "message":"One or more keys have the wrong type value",
            "expected": {key:self.data_types[value] for (key,value) in expected.items()},

            "received": {key:self.data_types[type(value)] for (key,value) in received_data.items()}
        }
        super().__init__(self.message)


class WrongKeysError(Exception):
    def __init__(self, received_data:dict,expected:dict):
        self.message = {
            "message":"One or more mandatory keys is missing",
            "expected": list(expected.keys()),
            "received": list(received_data.keys())
        }
        super().__init__(self.message)


class InvalidEmailError(Exception):
    def __init__(self):
        self.message ={"message": "Invalid Email"}
        super().__init__(self.message)


class NotFoundError(Exception):
    def __init__(self):
        self.message = {
            "message": "User not found"
        }
        super().__init__(self.message)
