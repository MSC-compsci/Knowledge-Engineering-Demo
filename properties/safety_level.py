from enum import Enum

from properties.desired_property import DesiredProperty

#Definition of Safety enumeration
class SafetyValue(Enum):
    ANY = 'any'
    AVG = 'average'
    SAFE = 'safest'


class SafetyLevel(DesiredProperty):
    #Constructor for SafetyLevel class
    def __init__(self, is_required: bool, min_level: SafetyValue):
        super().__init__(is_required)
        self.min_level = min_level
