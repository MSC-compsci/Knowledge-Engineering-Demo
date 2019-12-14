from enum import Enum

from properties.desired_property import DesiredProperty


class POI(Enum):
    SHOP = "Shop"
    MEDICAL_FACILITY = "Medical Facility"
    SWIMMING_POOL = "Swimming Pool"
    SCHOOL = "School"
    CINEMA = "Cinema"
    PUBLIC_TRANSPORT = "Public Transport"


class PointOfInterest(DesiredProperty):
    def __init__(self, is_required: bool, poi_type: POI):
        super().__init__(is_required)
        self.poi_type = poi_type
