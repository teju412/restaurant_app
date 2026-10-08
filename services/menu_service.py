def find_menu_item(menu_data, item_name):
    for menu_item in menu_data.values():
        if menu_item["item_name"].lower() == item_name:
            return menu_item

    return None