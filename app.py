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
    if item_name == "":
        print("Please enter an item name.")
        continue

    result = menu_service.find_menu_item(menu_data, item_name)
    # print(result)

    if result is None:
        print("Item not found.Please choose an item from the menu.")
        for menu_item in menu_data.values():
            print(f"{menu_item['item_name']} - Price: {menu_item['price']}")
    else:
        while True:
            try:
                quantity = int(input("Enter quantity: "))
            except ValueError:

                print("Invalid quantity. Please enter a valid number.")
                continue
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
            break
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
        


       