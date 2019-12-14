# Import the necessary packages
from typing import List

from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import FunctionItem

from properties.desired_property import DesiredProperty
from properties.poi import POI, PointOfInterest
from properties.proximity_to_work import ProximityToWork
from properties.rent import Rent
from properties.safety_level import SafetyLevel, SafetyValue
from queries import get_recommended_neighbourhoods

DESIRED_PROPERTY_OPTIONS = {
    "POI": 0,
    "Rent": 1,
    # "Proximity to work": 2,
    # "Safety Level": 3
}

POI_OPTIONS = [
    POI.SHOP.value,
    POI.MEDICAL_FACILITY.value,
    POI.SWIMMING_POOL.value,
    POI.SCHOOL.value,
    POI.CINEMA.value,
    POI.PUBLIC_TRANSPORT.value,
]


def is_required_prompt() -> bool:
    required_flag = input(
        "Is this selection a requirement or a preference?\nAnswer with (r) for requirement and (p) for preference\n")
    return required_flag == "r"


def poi_type_selection_handler() -> DesiredProperty:
    selected_poi_value = POI_OPTIONS[SelectionMenu.get_selection(POI_OPTIONS)]
    is_required = is_required_prompt()

    return PointOfInterest(poi_type=POI(selected_poi_value), is_required=is_required)


def rent_handler() -> DesiredProperty:
    min_value = int(input("What's the minimum rent (euro) you are willing to pay?\n"))
    max_value = int(input("What's the maximum rent (euro) you are willing to pay?\n"))
    is_required = is_required_prompt()

    return Rent(min_value=min_value, max_value=max_value, is_required=is_required)


def proximity_handler() -> DesiredProperty:
    max_distance = int(input("What's the maximum distance (in km) you are willing to commute on a daily basis?\n"))
    is_required = is_required_prompt()

    return ProximityToWork(max_distance=max_distance, is_required=is_required)


def safety_handler() -> DesiredProperty:
    min_level = input("What's the desired level of safety you want to have? Answer with any | average | safest\n")
    is_required = is_required_prompt()

    return SafetyLevel(min_level=SafetyValue(min_level), is_required=is_required)


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


def view_suggestions_func(desired_properties: List[DesiredProperty]):
    recommended_neighbourhoods = get_recommended_neighbourhoods(desired_properties, 10)

    print("List of recommended neighbourhoods:")

    for idx, neighbourhood in enumerate(recommended_neighbourhoods, 1):
        print(f"{idx}. {neighbourhood}")

    input("Press any Enter to go back..")


def main():
    desired_properties: List[DesiredProperty] = []

    # Create the menu
    menu = ConsoleMenu("AreA", "An advisor on Amsterdam's residential areas")

    # Menu Items
    desired_prop_item = FunctionItem("Add desired property", desired_prorerty_submenu, [desired_properties])
    view_sugg_item = FunctionItem("Get suggestions", view_suggestions_func, [desired_properties])

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(desired_prop_item)
    menu.append_item(view_sugg_item)

    # start menu
    menu.show()


if __name__ == '__main__':
    main()