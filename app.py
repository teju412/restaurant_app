import json
from services import menu_service

with open("data/menu.json", "r") as f:
    menu_data = json.load(f)

item_name = input("Enter item name: ").lower().strip()

result = menu_service.find_menu_item(menu_data, item_name)

if result is None:
    print("Item not found")
else:
    quantity = input("Enter quantity: ")
    amount = float(result["price"]) * int(quantity)
    order = {
        "item_name": result["item_name"],
        "price": result["price"],
        "quantity": quantity,
        "amount": amount
    }

    print("Order details:")
    print(f"Item Name: {order['item_name']}")
    print(f"Price: {order['price']}")
    print(f"Quantity: {order['quantity']}")
    print(f"Amount: {order['amount']}")