from typing import List

import pandas as pd

from properties.desired_property import DesiredProperty
from properties.poi import PointOfInterest, POI
from properties.rent import Rent

CURRENT_SCORE_COLUMN = 'current_score'

#This function opens the data provided in data folder and fills a list
def get_recommended_neighbourhoods(properties: List[DesiredProperty], number: int = 10) -> List[str]:
    amsterdam_neighbourhoods = pd.read_csv("data/amsterdam.csv")
    amsterdam_neighbourhoods[CURRENT_SCORE_COLUMN] = 0

    for prop in properties:
        if type(prop) is Rent:
            amsterdam_neighbourhoods = apply_rent(prop, amsterdam_neighbourhoods)
        if type(prop) is PointOfInterest:
            amsterdam_neighbourhoods = apply_poi(prop, amsterdam_neighbourhoods)

    amsterdam_neighbourhoods = amsterdam_neighbourhoods.sort_values(by=CURRENT_SCORE_COLUMN, ascending=False)

    return list(amsterdam_neighbourhoods['regio'].head(number))

#If rent is a requirement/preference this function is invoked
def apply_rent(rent: Rent, neighbourhoods: pd.DataFrame) -> pd.DataFrame:
    if rent.is_required:
        return neighbourhoods[neighbourhoods['rent_monthly'].between(rent.min_value, rent.max_value)]
    else:
        neighbourhoods.loc[neighbourhoods['rent_monthly'].between(rent.min_value, rent.max_value), CURRENT_SCORE_COLUMN] += 1
    return neighbourhoods

#If PointOfInterest is a requirement/preference this function is invoked
def apply_poi(poi: PointOfInterest, neighbourhoods: pd.DataFrame) -> pd.DataFrame:
    neighbourhood_filter = None

    if poi.poi_type == POI.PUBLIC_TRANSPORT:
        neighbourhood_filter = neighbourhoods['distance_train_station_meters'] <= 1000
    if poi.poi_type == POI.SHOP:
        neighbourhood_filter = neighbourhoods['supermarkets_1km'] >= 1
    if poi.poi_type == POI.CINEMA:
        neighbourhood_filter = neighbourhoods['cinemas_5km'] >= 1
    if poi.poi_type == POI.SWIMMING_POOL:
        neighbourhood_filter = neighbourhoods['distance_swimming_pool_meters'] <= 1000
    if poi.poi_type == POI.MEDICAL_FACILITY:
        neighbourhood_filter = (neighbourhoods['GP_1km'] >= 1) & (neighbourhoods['hospital_distance'] <= 1000)
    if poi.poi_type == POI.SCHOOL:
        neighbourhood_filter = neighbourhoods['schools_1km'] >= 1

    if poi.is_required:
        return neighbourhoods[neighbourhood_filter]
    else:
        neighbourhoods.loc[neighbourhood_filter, CURRENT_SCORE_COLUMN] += 1
    return neighbourhoods


if __name__ == '__main__':
    print(get_recommended_neighbourhoods([Rent(True, 0, 1000), PointOfInterest(False, POI.MEDICAL_FACILITY)]))
