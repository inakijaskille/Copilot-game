"""
Space station inventory management system.
"""

# Dictionary representing space station supplies with quantities
space_station_inventory = {
    "oxygen_tanks": 45,
    "water_liters": 320,
    "food_rations": 128,
    "medical_supplies": 87,
    "fuel_units": 200
}


def check_inventory(item):
    """
    Check if an item exists in the inventory and print its quantity.
    
    Args:
        item (str): The name of the item to check
    """
    if item in space_station_inventory:
        quantity = space_station_inventory[item]
        print(f"✓ {item}: {quantity} units in stock")
    else:
        print(f"✗ {item}: Not found in inventory")


# Main inventory check loop
if __name__ == "__main__":
    print("=== Space Station Inventory Check ===\n")
    
    # Items to check (at least three different items)
    items_to_check = ["oxygen_tanks", "food_rations", "backup_generators", "water_liters"]
    
    # Loop through and check each item
    for item in items_to_check:
        check_inventory(item)
