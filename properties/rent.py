from properties.desired_property import DesiredProperty


class Rent(DesiredProperty):
    def __init__(self, is_required: bool, min_value: int, max_value: int):
        super().__init__(is_required)
        self.min_value = min_value
        self.max_value = max_value
