"""
A program that is able to ADD,delete, list, inquire and purchase items from a dictionary.
"""
print("Welcome to my store")

unit_price = {1: 11.97, 2: 13.22, 3: 30.50}

description= {1: "laptop", 2: "gaming pc", 3: "tablet"}

inventory= {1: 300, 2: 593, 3:30}

inv_description = {v: k for k, v in description.items()}

dict = open("dict.txt", "r")

customerpri= []
customerq = []
customerd = []
def list():
    for i in description:
        print ("we have", description[i], '---id number---', i)

    menu()

def inquire ():
    x = 0
    product = input("what product do you want to know about ? ")
    for i in description:
        if description[i] == product:
            x = i
    if x == 0:
        print("Sorry, product is not availible")
    if x > 0:
        print(description[x], " has", inventory[x], "items in stock"
              + str("\n") +str("$") + str(unit_price[x]), "is the unit price per unit")
    menu()

def add():
    item = input("What item would you like to add? ").lower()
    x = 0
    for i in description:
        if item == description[i]:
            print("We already have that product")
            x = i
    if x == 0:
        description[len(description)+1] = item
        try:
            newprice = float(input("What is the unit_price of the product? "))
            unit_price[len(unit_price)+1] = newprice
            newinv = int(input("How many units are there of the product? "))
            inventory[len(inventory)+1] = newinv
        except ValueError:
            print("That is not a valid input, please try again. ")
            add()
    menu()

def receipt():
    fullprice = 0
    for i in range (len(customerq)):
        print("\nThank You, You purchased,"+ " "+ str(customerd[i]) +" "+ "with" +" "+ str(customerq[i]) +" "+ "items." )
        price = int((customerq[i]) * customerpri[i])
        fullprice += int(price)
    print("your subtotal is $"+ str(fullprice))
    print ("your total is $" + str(round(1.13*fullprice,2)))

def purchase():
    item = input("\nWhat product are you looking to purchase?").lower()
    v=0
    for i in description:
        if item == description[i]:
            v = v + 1
            quantity = int(input("How many of the item?"))
            if quantity > inventory[i]:
                print("Not Enough in Stock")
                purchase()
            if quantity <= inventory[i]:
                inventory[i] = inventory[i] - quantity
                customerd.append(item)
                for x in description:
                    if item == description[x]:
                        g = unit_price[x]
                        customerpri.append(g)
                        customerq.append(quantity)
            else:
                print("try again")
                purchase()
    if v==0:
        print("please try again")
        purchase()
    continueshop = input("\nWould you like to purchase anything else ").lower()
    if continueshop in ['y','ye','yes']:
        purchase()
    elif continueshop in ['n','no','nien']:
        receipt()
    else:
        print("try again")
        purchase()

    menu()

def delete():
    item = input("Which item do you want to remove ? ").lower()
    n = 0
    for i in description:
        if item == description[i]:
            n = i
    if n == 0:
        print("we do not have that product")
    if n!= 0:
        del description[n]
        del unit_price[n]
        del inventory[n]
        print("That item has been removed")
    menu()

def menu():
    choice = input("\nWhat would you like to do? \nList, Inquire, Delete, Add, Purchase or Exit:\n").lower()
    if choice in ['list','l','lis','li']: list()
    elif choice in ['inquire','i','inq','in']: inquire()
    elif choice in ['delete','d','del','de', 'dele']: delete()
    elif choice in ['add','ad', 'a']: add()
    elif choice in ['purchase', 'purch','pur', 'p']: purchase()
    elif choice in ['exit','e','ex']:
        print("Thank you for Visiting the microsoft Store ")
    else:
        print("Sorry that is not a valid option \nPlease try Again ")
        menu()

menu()



