#list of menu from which the user can order pizza
Menu = {"cheese pizza", "veggie pizza" , "pepperoni pizza", "meat pizza", "bbq chicken pizza"}
#getting order
current_order = []
print("              Welcome        ")
def menu():
#The main menu
  mode = input("""What would you like to do? Please insert the number:
  1: Make an order
  2: My orders
  3: view Menu
  4: Exit
  """).strip()

  return mode
#Function that allows user to order
def get_order():
    while True:
        order = input("What can I get for you?").strip().lower()
        if order in Menu:
            current_order.append(order)
        else:
            print("Sorry we don't serve that")
            continue
        if is_order_complete():
            return current_order
def is_order_complete():
    choice = input("Do you want anything else? Please answer with yes/no")
    if choice == "no":
        return True
    elif choice == "yes":
        return False
    else:
        raise Exception("invalid input")

def view_order():
    print("So your order is: ")
    for order in current_order:
        print(order)


while True:
    chosen_option = menu()

    if chosen_option == "1":
        get_order()
    elif chosen_option == "2":
        view_order()
    elif chosen_option == "3":
        print(*Menu, sep = ", ")
    elif chosen_option == "4":
        break
    else:
        print("That wasn't an option, please try again")
print("Goodbye!")
