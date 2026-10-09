import json
from services import menu_service

with open("data/menu.json", "r") as f:
    menu_data = json.load(f)

orders = []
total_amount = 0
print("===== Welcome to Our Restaurant =====")
print("===== Menu =====")
categories = ["Starter", "Fast Food", "Main Course", "Bread", "Beverage"]

for category in categories:
    print(f"\n--- {category} ---")
    for menu_id, menu_item in menu_data.items():
        if menu_item["category"] == category:
            print(f"{menu_id}.{menu_item['item_name']} - Price: ₹{menu_item['price']}")

print("Type 'exit' to finish your order.")

while True:
    menu_id = input("Enter item ID: ").strip()

    if menu_id == "exit":
        break
    if menu_id == "":
        print("Please enter an item ID.")
        continue

    result = menu_data.get(menu_id)
    # result = menu_service.find_menu_item(menu_data, menu_id)
    # print(result)

    if result is None:
        print("Item not found. Please choose an item from the menu.")
        for menu_id, menu_item in menu_data.items():
            print(f"{menu_id}. {menu_item['item_name']} - Price: ₹{menu_item['price']}")
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
        


       