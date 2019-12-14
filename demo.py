# Import the necessary packages
from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import FunctionItem, SelectionItem, SubmenuItem

DESIRED_PROPERTY_OPTIONS = {"POI": 0, "Rent": 1, "Proximity to work": 2, "Safety Level": 3 }

def poiSelectionHandler():
    pass

def rentSelectionHandler():
    pass

def proxSelectionHandler():
    pass

def safetySelectionHandler():
    pass

def desPropFunc():
    selected = SelectionMenu.get_selection(DESIRED_PROPERTY_OPTIONS.keys())
    if selected == DESIRED_PROPERTY_OPTIONS["POI"]:
        poiSelectionHandler()
    elif selected == DESIRED_PROPERTY_OPTIONS["Rent"]:
        rentSelectionHandler()
    elif selected == DESIRED_PROPERTY_OPTIONS["Proximity to work"]:
        proxSelectionHandler()
    elif selected == DESIRED_PROPERTY_OPTIONS["Safety Level"]:
        safetySelectionHandler()


def resListFunc():
    print("resListFunc")

# Create the menu
menu = ConsoleMenu("AreA", "An advisor on Amsterdam's residential areas")

# Menu Items

desPropItem = FunctionItem("Choose property", desPropFunc)
#desProp = SubmenuItem("Add desired property", selectionMenu, menu)
resListItem = FunctionItem("Get suggestions", resListFunc)


# Once we're done creating them, we just add the items to the menu
menu.append_item(desPropItem)
menu.append_item(resListItem)


#start menu
menu.show()