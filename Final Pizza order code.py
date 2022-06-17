import TableIt
TableIt.initColors()

# pizza menu list with id and prices
PIZZA_LIST = [
    ['ITEM #','PIZZA','COST'],
    [1,'cheese pizza',8.50],[2,'veggie pizza',8.50], [3,'pepperoni pizza',8.50],[4,'Beyound Beef supreme',8.50],[5,'BBQ chicken pizza',8.50],
    [6,'margarita',8.50],[7,'bombay chicken pizza',8.50],[8,'butter chicken pizza',13.5],[9,'bolognese',13.5],[10,'spicy italian pizza',13.5],[11,'meat lovers',13.5],[12,'italian lovers',13.5]
]

# list of toppings to add to pizzas
TOPPING_LIST = [['ITEM #','TOPPING','COST'],[1,'extra cheese',0.5], [2,'onions', 0.5], [3,'green pepper',0.5], [4,'mushroom',0.5]]

# delivery cost
delivery_cost = 3

# user-input lists
yes_list = ["yes","yeah","y","sure","okay","ok","k"]
no_list = ["no","nah","nope","n","never","i don't think so"]

# list for costs
sub_total = [] # cost of pizzas and toppings
final_order = [] # sub total cost + delivery charges

# list of order
current_pizza_order = []
current_topping_order = []
# Function to show Order Menu
def ShowMenu():
    print("Available Pizzas:\n")
    TableIt.printTable(PIZZA_LIST,useFieldNames=True, color=(230, 110, 150))
    print("\n\nAvailable Topings:\n")
    TableIt.printTable(TOPPING_LIST,useFieldNames=True, color=(230, 110, 150))
    print('\n\n')

# Function to get customer Order
def TakeOrderInput():    
    chosenPizza = ''
    chosenPizzaPrice = 0
    chosenTopping = ''
    chosenToppingPrice = 0
    
    while True:
        #runs the ShowMenu function and displays the table for the users 
        ShowMenu()
        while chosenPizza == "":
            try:
                print("ATTENTION!!, at any stage if you would like to cancel your order just type 0")
                pizza = int(input("Please choose a pizza using Item Number: "))
                #search if pizza in PIZZA_LIST:
                for x in PIZZA_LIST:
                        if x[0] == int(pizza): 
                            chosenPizza = x[1]
                            current_pizza_order.append(PIZZA_LIST[pizza])
                            chosenPizzaPrice = x[2]
                            sub_total.append(chosenPizzaPrice)
                            print("Your Choice: ", chosenPizza)
                            print("Cost: $", chosenPizzaPrice)
                            break
                        if x not in PIZZA_LIST:
                            print("invalid entry")
                            break
                #code to allow the users to cancel their orders        
                if pizza == 0:
                    print("order canceled")
                    exit()
            except ValueError:
                        print("invalid entry, please check your response")
        #Codes for extra topping 
        while chosenTopping == "":
            try:
                topping = int(input("Please choose a pizza topping using Item Number: "))
                for x in TOPPING_LIST:
                    if x[0] == int(topping):
                        chosenTopping = x[1]
                        current_topping_order.append(TOPPING_LIST[topping])
                        chosenToppingPrice = x[2]
                        sub_total.append(chosenToppingPrice)
                        print("Your Choice: ", chosenTopping)
                        print("Cost: $",chosenToppingPrice)
                        break
                #code to allow the users to cancel their orders     
                if topping == 0:
                    print("order canceled")
                    exit()
            except ValueError:
                        print("invalid entry, please check your response")
        #Code for extra pizza order 
        while True:
            extra_pizza = input("Would you like to order another pizza?").strip().lower()
            if extra_pizza in no_list:
                print("You ordered {} with {}".format(chosenPizza, chosenTopping))
                print("")
                break
            #code for canceling the order and exiting 
            elif extra_pizza == "0":
                    print("order canceled")
                    exit()
            elif extra_pizza not in yes_list and extra_pizza not in no_list:
                print("invalid input")
            if extra_pizza in yes_list:
                try:
                    while True:
                        more_pizza = int(input("How many more pizzas would you like to order? "))
                        if int(more_pizza) < 0 or int(more_pizza) > 5:
                            print("You can only make up to 5 orders only")
                            continue
                        elif int(more_pizza) > 0 and int(more_pizza) < 5:
                            print("please insert the ITEM # number to order.")
                            for x in range (more_pizza):
                                customer_extra_pizza =  int(input("pizza: "))
                                extra_topping = int(input("topping: "))
                                for x in PIZZA_LIST:
                                    if x[0] == int(customer_extra_pizza):
                                        chosenPizza = x[1]
                                        chosenPizzaPrice = x[2]
                                        sub_total.append(chosenPizzaPrice)
                                for x in TOPPING_LIST:
                                    if x[0] == int(extra_topping):
                                        chosenTopping = x[1]
                                        chosenToppingPrice = x[2]
                                        sub_total.append(chosenToppingPrice)
                                        print("You ordered {} with {}".format(chosenPizza, chosenTopping))
                                        total_cost = chosenPizzaPrice + chosenToppingPrice
                                        print("Cost: $", total_cost)
                            break
                        if int(more_pizza) == 0:
                                print("order canceled")
                                exit()
                except ValueError:
                    print("invalid entry, please check your response")
                    continue
                break
        #code for calculating the total cost of order 
        all_pizza_cost = sum(sub_total)    
        #code for displaying the cost to user
        print('Your order total is $', all_pizza_cost)
        #code for delivery 
        while True:
            try:
                Delivery = input("Do you want this order delivered? ").strip().lower()
                #code for delivery if the user wants it delivered. 
                if Delivery in yes_list:
                    #adding the cost of delivery to the total cost.
                    Full_cost = all_pizza_cost + delivery_cost
                    #taking customer name
                    customer_name = input("please insert your name: ").title()
                    if customer_name == "0":
                        print("order canceled")
                        exit()
                    #code customer contact number
                    customer_contact_number = int(input("please insert your contact number: "))
                    if customer_contact_number == 0:
                        print("order canceled")
                        exit()
                    #code for customer address
                    customer_address = input("please insert your address: ")
                    if customer_address == "0":
                        print("order canceled")
                        exit()
                    print("                    ")
                    #displaying the total pizza order cost, delivery charge and overall total cost
                    print("Your pizza order cost is ${} \nDelivery charge is $3 \nTotal Cost is ${}".format(all_pizza_cost, Full_cost))
                    print("Thank you for your order {}.Soon we will deliver your order to {} \n"
                            "and the delivery guy will contact you on {}".format(customer_name, customer_address, customer_contact_number))
                    break
                #Not for delivery 
                if Delivery in no_list:
                    customer_name = input("please insert your name: ").title()
                    if customer_name == "0":
                            print("order canceled")
                            exit()
                    print("Thank you for your order {}. The total cost of your order is {}. You can pick it up from Henderson Pizza shop".format(customer_name, all_pizza_cost))
                    break
                #Cancel order and exit
                if Delivery == "0":
                    print("order canceled")
                    exit()
            except ValueError:
                print("invalid input, please check your input")
                continue

TakeOrderInput()
