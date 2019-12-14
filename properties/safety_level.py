from properties.desired_property import DesiredProperty


class SafetyLevel(DesiredProperty):
    def __init__(self, is_required: bool, min_level: str):
        super().__init__(is_required)
        self.min_level = min_level
