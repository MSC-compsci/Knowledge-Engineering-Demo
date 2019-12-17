from properties.desired_property import DesiredProperty


class ProximityToWork(DesiredProperty):
    #constructor for ProximityToWork class
    def __init__(self, is_required: bool, max_distance: int):
        super().__init__(is_required)
        self.max_distance = max_distance
