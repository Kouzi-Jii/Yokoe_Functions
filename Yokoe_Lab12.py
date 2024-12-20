MenuItem = [{"id":"Cheese Burger", "price": 55.00},
            {"id":"Fried Chicken", "price": 120.00},
            {"id":"Pizza", "price": 250.00},
            {"id":"CocaCola", "price": 78.25},
            {"id":"Coffee", "price": 65.90},
            {"id":"Icecream", "price": 90.82}]  #declares a dictionary
picked_item = [] #declares a list

def dis_menu(): #first function for showing the menu
    print("\nOur Food Menu:")
    num = 1
    for food in MenuItem:
        print(f"{num}. {food["id"]} - ₱{food["price"]}")
        num += 1

def pick_food(): #second function for asking the user for their order
    while True:
        dis_menu()
        bought = int(input("\nPlease enter the number of your chosen item from our menu:"))
        if bought <= 6 and bought >= 1:
            index = bought - 1
            picked_item.append(MenuItem[index])
            break
        else:
            print("\nInvalid input. Please try again.")
    
    
def pay_food(): #third function for calculating the price of the item and asking for payment
    while True:
        total = 0
        for item in picked_item:
            print(f"\nYour {item["id"]} costs ₱{item["price"]}!")
            total += item["price"]
        payment = float(input(f"Please enter the amount you wish to pay: ₱"))
        if payment >= total:
            change = payment - total
            if change > 0:
                print(f"\nYour Change is ₱{round(change,2)}!")
                print(f"Thank you for your purchase, your order will be prepared shortly!")
            break
        else:
            print("The amount you entered is insufficient. Please try again and enter a sufficient ammount.")

def process(): #The whole process function
    pick_food()
    pay_food()

process()