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

        amount = result["price"] * quantity
        total_amount += amount

        order = {
            "item_name": result["item_name"],
            "price": result["price"],
            "quantity": quantity,
            "amount": amount,
           
        }

        orders.append(order)

print(orders)
for order in orders:
    print(f"Item Name: {order['item_name']}, Price: {order['price']}, Quantity: {order['quantity']}, Amount: {order['amount']}")
print(f"Total Amount: {total_amount}")   