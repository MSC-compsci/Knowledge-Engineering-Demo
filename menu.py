# Import the necessary packages
from typing import List
import pandas as pd

from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import FunctionItem

from properties.desired_property import DesiredProperty
from properties.poi import POI, PointOfInterest
from properties.proximity_to_work import ProximityToWork
from properties.rent import Rent
from properties.safety_level import SafetyLevel, SafetyValue
from queries import get_recommended_neighbourhoods

#Dictionary containing the Desired Property types
DESIRED_PROPERTY_OPTIONS = {
    "POI": 0,
    "Rent": 1,
    # "Proximity to work": 2,
    # "Safety Level": 3
}

#Enumeration containing the poi types
POI_OPTIONS = [
    POI.SHOP.value,
    POI.MEDICAL_FACILITY.value,
    POI.SWIMMING_POOL.value,
    POI.SCHOOL.value,
    POI.CINEMA.value,
    POI.PUBLIC_TRANSPORT.value,
]

# User specifies whether the input is a requirement or a preference
def is_required_prompt() -> bool:
    required_flag = input(
        "Is this selection a requirement or a preference?\nAnswer with (r) for requirement and (p) for preference\n")
    return required_flag == "r"

#Handles the type of the Point of Interest
def poi_type_selection_handler() -> DesiredProperty:
    selected_poi_value = POI_OPTIONS[SelectionMenu.get_selection(POI_OPTIONS)]
    is_required = is_required_prompt()

    return PointOfInterest(poi_type=POI(selected_poi_value), is_required=is_required)

#Prompts the user to provide min and max rent, stores the input on a Rent object
def rent_handler() -> DesiredProperty:
    min_value = int(input("What's the minimum rent (euro) you are willing to pay?\n"))
    max_value = int(input("What's the maximum rent (euro) you are willing to pay?\n"))
    is_required = is_required_prompt()

    return Rent(min_value=min_value, max_value=max_value, is_required=is_required)

#Prompts the user to provide the max distance they want to travel daily, stores the input on a ProximityToWork object
def proximity_handler() -> DesiredProperty:
    max_distance = int(input("What's the maximum distance (in km) you are willing to commute on a daily basis?\n"))
    is_required = is_required_prompt()

    return ProximityToWork(max_distance=max_distance, is_required=is_required)

#Creates and stores user's safety level choice
def safety_handler() -> DesiredProperty:
    min_level = input("What's the desired level of safety you want to have? Answer with any | average | safest\n")
    is_required = is_required_prompt()

    return SafetyLevel(min_level=SafetyValue(min_level), is_required=is_required)

#Creates a submenu for the desired property
def desired_prorerty_submenu(desired_properties: List[DesiredProperty]):
    selected = SelectionMenu.get_selection(DESIRED_PROPERTY_OPTIONS.keys())
    if selected == DESIRED_PROPERTY_OPTIONS["POI"]:
        new_property = poi_type_selection_handler()
    elif selected == DESIRED_PROPERTY_OPTIONS["Rent"]:
        new_property = rent_handler()
    elif selected == DESIRED_PROPERTY_OPTIONS["Proximity to work"]:
        new_property = proximity_handler()
    elif selected == DESIRED_PROPERTY_OPTIONS["Safety Level"]:
        new_property = safety_handler()
    else:
        return
    desired_properties.append(new_property)

#Function responsible to print recommended neighboorhoods
def view_suggestions_func(neighbourhoods: pd.DataFrame, desired_properties: List[DesiredProperty]):
    recommended_neighbourhoods = get_recommended_neighbourhoods(neighbourhoods, desired_properties, 10)

    print("List of recommended neighbourhoods:")

    for idx, neighbourhood in enumerate(recommended_neighbourhoods, 1):
        print(f"{idx}. {neighbourhood}")

    input("Press any Enter to go back..")

#The main fuction: The console menu is created, an then the rest of the submenus are attached to it.
def main():
    #List containing the choices of the user
    desired_properties: List[DesiredProperty] = []

    #Load ontology
    amsterdam_neighbourhoods = pd.read_csv("data/amsterdam.csv")

    # Create the menu
    menu = ConsoleMenu("AreA", "An advisor on Amsterdam's residential areas")

    # Menu Items
    desired_prop_item = FunctionItem("Add desired property", desired_prorerty_submenu, [desired_properties])
    view_sugg_item = FunctionItem(
        "Get suggestions",
        view_suggestions_func,
        [amsterdam_neighbourhoods, desired_properties]
    )

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(desired_prop_item)
    menu.append_item(view_sugg_item)

    # start menu
    menu.show()


if __name__ == '__main__':
    main()