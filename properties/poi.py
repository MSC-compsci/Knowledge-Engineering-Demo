from enum import Enum

from properties.desired_property import DesiredProperty

#Creates an emunaration of points of interest
class POI(Enum):
    SHOP = "Shop"
    MEDICAL_FACILITY = "Medical Facility"
    SWIMMING_POOL = "Swimming Pool"
    SCHOOL = "School"
    CINEMA = "Cinema"
    PUBLIC_TRANSPORT = "Public Transport"

class PointOfInterest(DesiredProperty):
    #Constructor for the PointOfInterest class
    def __init__(self, is_required: bool, poi_type: POI):
        super().__init__(is_required)
        self.poi_type = poi_type
