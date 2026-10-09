import json
from services import menu_service

with open("data/menu.json", "r") as f:
    menu_data = json.load(f)

orders = []
total_amount = 0

while True:
    item_name = input("Enter item name: ").lower().strip()

    if item_name == "exit":
        break

    result = menu_service.find_menu_item(menu_data, item_name)

    if result is None:
        print("Item not found")
    else:
        quantity = int(input("Enter quantity: "))
        item_exists = False
        for order in orders:
            if order["item_name"] == result["item_name"]:
                order["quantity"] += quantity
                order["amount"] = order["price"] * order["quantity"]
                item_exists = True
                break
        if not item_exists:
            # Create the order dictionary
            order = {
                "item_name": result["item_name"],
                "price": result["price"],
                "quantity": quantity,
                "amount": result["price"] * quantity
            }
            # Append it to orders
            orders.append(order)
print("Order Summary:")
for order in orders:
    print(f"{order['item_name']} - Quantity: {order['quantity']}, Amount: {order['amount']}")
    total_amount += order["amount"]
print(f"Total Amount: {total_amount}")
        


       