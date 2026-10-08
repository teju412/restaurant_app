import json
from services import menu_service

with open("data/menu.json", "r") as f:
    menu_data = json.load(f)

item_name = input("Enter item name: ").lower().strip()

result = menu_service.find_menu_item(menu_data, item_name)

if result is None:
    print("Item not found")
else:
    print("Item:", result["item_name"])
    print("Category:", result["category"])
    print("Price:", result["price"])