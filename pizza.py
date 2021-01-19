class Pizza:
    def __init__(self,id=0, topping1="", topping2="", topping3="", status="unserved"):
        id_list = []
        self.topping1 = topping1
        self.topping2 = topping2
        self.topping3 = topping3
        self.status = status
        self.id = id

    def add_pizza(self, pizza_dict):
        pizza_list = []
        pizza_dict[self.id] = self.topping1, self.topping2, self.topping3, self.status
        pizza_list.append(pizza_dict[self.id])
        return pizza_list

def choose_pizza(pizza_dict):
    for id in pizza_dict:
        print("{}. {:<8} --- Pizza with {} {} {}".format(id, pizza_dict[id][3], pizza_dict[id][0], pizza_dict[id][1], pizza_dict[id][2]))
    choose_input = int(input("choose pizza: "))
    for id in pizza_dict:
        if id == choose_input:
            pizza_list = list(pizza_dict[id])
            pizza_list[3] = "served"
            pizza_dict[id] = pizza_list
    return pizza_dict

def remove_all_served(pizza_dict):
    for id in list(pizza_dict):
        if pizza_dict[id][3] == "served":
           pizza_dict.pop(id)
    return pizza_dict

def print_pizza(pizza_dict):
    for id in pizza_dict:
        print("{}. {:<8} --- Pizza with {} {} {}".format(id, pizza_dict[id][3], pizza_dict[id][0], pizza_dict[id][1], pizza_dict[id][2]))

def clear():
    return print("\n" * 30)

pizza_dict = {}
id = 0
toping1 = ""
toping2 = ""
toping3 = ""

pizza1 = Pizza(1, "pepperoni", "cheese")
pizza2 = Pizza(2, "ham", "bacon", "chicken")
pizza3 = Pizza(3, "extra-cheese")
pizza4 = Pizza(4, "pepperoni", "pinapple")
pizza5 = Pizza(5, "beans", "bacon", "eggs")
pizza6 = Pizza(6, "no sauce", "no cheese", "no bread")


pizza_input = input
pizza1.add_pizza(pizza_dict)
pizza2.add_pizza(pizza_dict)
pizza3.add_pizza(pizza_dict)
pizza4.add_pizza(pizza_dict)
pizza5.add_pizza(pizza_dict)
pizza6.add_pizza(pizza_dict)

while pizza_input != "q":
    print("1. list of pizza\n2. choose pizza\n3. remove all served\n4. add pizza\nq. Quit")
    pizza_input = input("input: ").lower()
    if pizza_input == "1":
        clear()
        print_pizza(pizza_dict)
        print()
    elif pizza_input == "2":
        clear()
        choose_pizza(pizza_dict)
        clear()
    elif pizza_input == "3":
        clear()
        remove_all_served(pizza_dict)
        print()
    elif pizza_input == "4":
        clear()
        print_pizza(pizza_dict)
        print()
        id = int(input("ID: "))
        toping1 = input("Toping 1: ")
        toping2 = input("Toping 2: ")
        toping3 = input("Toping 3: ")
        new_pizza = Pizza(id, toping1, toping2, toping3)
        new_pizza.add_pizza(pizza_dict)
        print()
    elif pizza_input == "q":
        break
    else:
        print("Invalid input")
    print()
