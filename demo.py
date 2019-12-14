# Import the necessary packages
import time
from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import FunctionItem
from enum import Enum

class POI(Enum):
    SHOP = 1,
    MEDICAL_FACILITY = 2,
    SWIMMING_POOL = 3,
    SCHOOL = 4, 
    CINEMA = 5, 
    PUBLIC_TRANSPORT = 6

PropertyList = []

class DesiredProperty():
    #isRequired translates into preference
    def __init__(self, is_required: bool):
        self.is_required = is_required

class PointOfInterest(DesiredProperty):
    def __init__(self, is_required: bool, poi_type: POI):
        self.poi_type = poi_type
        self.is_required = is_required

class Rent(DesiredProperty):
    def __init__(self, is_required: bool, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        self.is_required = is_required

class ProximityToWork(DesiredProperty):
    def __init__(self, is_required: bool, max_distance: int):
        self.max_distance = max_distance
        self.is_required = is_required

class SafetyLevel(DesiredProperty):
    def __init__(self, is_required: bool, min_level: str):
        self.min_level = min_level
        self.is_required = is_required
        
    

DESIRED_PROPERTY_OPTIONS = {"POI": 0, "Rent": 1, "Proximity to work": 2, "Safety Level": 3 }
POI_OPTIONS = {"Shop": 0, "Medical Facility": 1, "Swimming Pool": 2, "School": 3, "Cinema": 4, "Public Transport": 5 }

def poi_type_selection_handler():
    selected = SelectionMenu.get_selection(POI_OPTIONS.keys())
    flag = input("Is this selection a requirement or a preference?\nAnswer with (r) for requirement and (p) for preference\n")
    if selected == POI_OPTIONS["Shop"] & int(flag == "r"):
        list_item = PointOfInterest(poi_type = POI.SHOP, is_required = True)
    else:
        list_item = PointOfInterest(poi_type = POI.SHOP, is_required = False)
    PropertyList.append(list_item)
    if selected == POI_OPTIONS["Medical Facility"] & int(flag == "r"):
        list_item = PointOfInterest(poi_type = POI.MEDICAL_FACILITY, is_required = True)
    else:
        list_item = PointOfInterest(poi_type = POI.MEDICAL_FACILITY, is_required = False)
    PropertyList.append(list_item)
    if selected == POI_OPTIONS["Swimming Pool"] & int(flag == "r"):
        list_item = PointOfInterest(poi_type = POI.SWIMMING_POOL, is_required = True)
    else:
        list_item = PointOfInterest(poi_type = POI.SWIMMING_POOL, is_required = False)
    PropertyList.append(list_item)
    if selected == POI_OPTIONS["School"] & int(flag == "r"):
        list_item = PointOfInterest(poi_type = POI.SCHOOL, is_required = True)
    else:
        list_item = PointOfInterest(poi_type = POI.SCHOOL, is_required = False)
    PropertyList.append(list_item)
    if selected == POI_OPTIONS["Cinema"] & int(flag == "r"):
        list_item = PointOfInterest(poi_type = POI.CINEMA, is_required = True)
    else:
        list_item = PointOfInterest(poi_type = POI.CINEMA, is_required = False)
    PropertyList.append(list_item)
    if selected == POI_OPTIONS["Public Transport"] & int(flag == "r"):
        list_item = PointOfInterest(poi_type = POI.PUBLIC_TRANSPORT, is_required = True)
    else:
        list_item = PointOfInterest(poi_type = POI.PUBLIC_TRANSPORT, is_required = False)
    PropertyList.append(list_item)


def rent_handler():
    min_value = input("What's the minimum rent you are willing to pay?\n")
    max_value = input("What's the maximum rent you are willing to pay?\n")
    flag = input("Is this selection a requirement or a preference?\n Answer with (r) for requirement and (p) for preference\n")
    if flag == "r":
        rent_Item = Rent(min_value = min_value,  max_value = max_value, is_required = True)
    else:
        rent_Item = Rent(min_value = min_value,  max_value = max_value, is_required = False)
    #print(rent_Item.min_value, rent_Item.max_value)
    #time.sleep(5)
    PropertyList.append(rent_Item)

def proximity_handler():
    max_distance = input("What's the maximum distance (in km) you are willing to commute on a daily basis?\n")
    flag = input("Is this selection a requirement or a preference?\n Answer with (r) for requirement and (p) for preference\n")
    if flag == "r":
        prox_Item = ProximityToWork(max_distance = max_distance, is_required = True)
    else:
        prox_Item = ProximityToWork(max_distance = max_distance, is_required = False)
    PropertyList.append(prox_Item)

def safety_handler():
    min_level = input("What's the desired level of safety you want to have? Answer with none | weak | strong\n")
    flag = input("Is this selection a requirement or a preference?\n Answer with (r) for requirement and (p) for preference\n")
    if flag == "r":
        safety_Item = SafetyLevel(min_level = min_level, is_required = True)
    else:
        safety_Item = SafetyLevel(min_level = min_level, is_required = False)
    PropertyList.append(safety_Item)

def desired_prorerty_func():
    selected = SelectionMenu.get_selection(DESIRED_PROPERTY_OPTIONS.keys())
    if selected == DESIRED_PROPERTY_OPTIONS["POI"]:
        poi_type_selection_handler()
    elif selected == DESIRED_PROPERTY_OPTIONS["Rent"]:
        rent_handler()
    elif selected == DESIRED_PROPERTY_OPTIONS["Proximity to work"]:
        proximity_handler()
    elif selected == DESIRED_PROPERTY_OPTIONS["Safety Level"]:
        safety_handler()


def view_suggestions_func():
    print("view_suggestions_func")

# Create the menu
menu = ConsoleMenu("AreA", "An advisor on Amsterdam's residential areas")

# Menu Items

desired_prop_item = FunctionItem("Choose property", desired_prorerty_func)
view_sugg_item = FunctionItem("Get suggestions", view_suggestions_func)


# Once we're done creating them, we just add the items to the menu
menu.append_item(desired_prop_item)
menu.append_item(view_sugg_item)


#start menu
menu.show()