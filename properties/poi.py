from enum import Enum

from properties.desired_property import DesiredProperty


class POI(Enum):
    SHOP = "Shop"
    MEDICAL_FACILITY = "Medical Facility"
    SWIMMING_POOL = "Swimming Pool"
    SCHOOL = "School"
    CINEMA = "Cinema"
    PUBLIC_TRANSPORT = "Public Transport"
    #
    # @classmethod
    # def from_name(cls, name):
    #     for station, station_name in STATIONS.items():
    #         if station_name == name:
    #             return station
    #     raise ValueError('{} is not a valid station name'.format(name))
    #
    # def to_name(self):
    #     return STATIONS[self.value]


class PointOfInterest(DesiredProperty):
    def __init__(self, is_required: bool, poi_type: POI):
        super().__init__(is_required)
        self.poi_type = poi_type
