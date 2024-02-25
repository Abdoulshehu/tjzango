from store import provision_items, provision_items2


def report():
    for item in provision_items2:
        all_item = provision_items2[item]
        for key in all_item:
            print(f"{key} : {all_item[key]} units")

def menu():
    menu_list =[]
    for item in provision_items:
       menu_list.append(item)
    print(menu_list)


def price():
    for item in provision_items2:
        all_item = provision_items2[item]
        for key in all_item:
            print(f"{key} : {all_item[key]} units")

def price():
     prices = []
     for item in provision_items:
        for keys in provision_items[item]:
            amnt = prices.append(keys)
        print(amnt)
price()
     
def place_order():
    add_to_cart = []
    order = input("Place your Order Here__").split()
    quantity = input("Enter Quantity Of Items").split()

    for item in order:
            # Confirm the availabity of the item in the store i.e "provition_items"
            # Create two list one for items available, the other else
            # Use your quantity input and confirm the avilable requested quantity is in stock 
            # Deduct form the provition item two
            # Calculate the total for each item and total for grand total 
            # Retun to user the items that were available and those that arn't 

            """
                Create a variable that will hold the available items (May be a list )
                NOT:: Create a variable that will hold the available items (May be a list )
                etc
            """
            add_to_cart.append(item)
    print(f"My Order:- {add_to_cart},")



is_on = True
while is_on:
        create_order = input("Type MENU here__ ").lower()
        if create_order == "report":
            report()
        elif create_order == 'menu':
            menu()
            place_order()







