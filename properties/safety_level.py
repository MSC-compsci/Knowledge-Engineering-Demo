from enum import Enum

from properties.desired_property import DesiredProperty


class SafetyValue(Enum):
    ANY = 'any'
    AVG = 'average'
    SAFE = 'safest'


class SafetyLevel(DesiredProperty):
    def __init__(self, is_required: bool, min_level: SafetyValue):
        super().__init__(is_required)
        self.min_level = min_level
