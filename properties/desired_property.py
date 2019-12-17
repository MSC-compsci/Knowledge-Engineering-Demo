class DesiredProperty():
    #Constructor for the DesiredProperty class
    #is_required = True means the object of this class is a requirement
    #is_required = False means the object of this class is a preference
    def __init__(self, is_required: bool):
        self.is_required = is_required
