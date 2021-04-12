PIZZA_DICT = {}
ID = 6

def clear():
    return print("\n" * 30)

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

class Order:
    def __init__(self, pizza_dict):
        self.pizza_dict = pizza_dict

    def choose_pizza(self, pizza_dict):
        pizza_dict = self.pizza_dict
        for id in pizza_dict:
            if pizza_dict[id][2]:
                print("{}. {:<8} --- Pizza with {}, {} and {}".format(id, pizza_dict[id][3], pizza_dict[id][0], pizza_dict[id][1], pizza_dict[id][2]))
            elif pizza_dict[id][1]:
                print("{}. {:<8} --- Pizza with {} and {}".format(id, pizza_dict[id][3], pizza_dict[id][0], pizza_dict[id][1]))
            else:
                print("{}. {:<8} --- Pizza with {}".format(id, pizza_dict[id][3], pizza_dict[id][0]))
        try:
            print()
            choose_input = int(input("choose pizza: "))
            if choose_input not in pizza_dict:
                print("\ninvalid input\n")
                self.choose_pizza(pizza_dict)
            else:
                for id in pizza_dict:
                    if id == choose_input:
                        pizza_list = list(pizza_dict[id])
                        pizza_list[3] = "served"
                        pizza_dict[id] = pizza_list
                return pizza_dict
        except ValueError:
            print()
            print("invalid input\n")
            self.choose_pizza(pizza_dict)

    def remove_all_served(self, pizza_dict):
        pizza_dict = self.pizza_dict
        counter = 1
        for id in list(pizza_dict):
            if pizza_dict[id][3] == "served":
               pizza_dict.pop(id)
        for id in list(pizza_dict):
            if (id - 1) not in pizza_dict and id != 1:
                pizza_dict[counter] = pizza_dict.pop(id)
            counter += 1
        return pizza_dict

    def print_pizza(self, pizza_dict):
        pizza_dict = self.pizza_dict
        for id in pizza_dict:
            if pizza_dict[id][2]:
                print("{}. {:<8} --- Pizza with {}, {} and {}".format(id, pizza_dict[id][3], pizza_dict[id][0], pizza_dict[id][1], pizza_dict[id][2]))
            elif pizza_dict[id][1]:
                print("{}. {:<8} --- Pizza with {} and {}".format(id, pizza_dict[id][3], pizza_dict[id][0], pizza_dict[id][1]))
            else:
                print("{}. {:<8} --- Pizza with {}".format(id, pizza_dict[id][3], pizza_dict[id][0]))

def main():
    global ID
    pizza1 = Pizza(1, "pepperoni", "cheese")
    pizza2 = Pizza(2, "ham", "bacon", "chicken")
    pizza3 = Pizza(3, "extra-cheese")
    pizza4 = Pizza(4, "pepperoni", "pinapple")
    pizza5 = Pizza(5, "beans", "bacon", "eggs")
    pizza6 = Pizza(6, "no sauce", "no cheese", "no bread")

    pizza_input = input
    pizza1.add_pizza(PIZZA_DICT)
    pizza2.add_pizza(PIZZA_DICT)
    pizza3.add_pizza(PIZZA_DICT)
    pizza4.add_pizza(PIZZA_DICT)
    pizza5.add_pizza(PIZZA_DICT)
    pizza6.add_pizza(PIZZA_DICT)

    order = Order(PIZZA_DICT)

    while pizza_input != "q":
        print("1. list of pizza\n2. choose pizza\n3. remove all served\n4. add pizza\nq. Quit")
        pizza_input = input("input: ").lower()
        if pizza_input == "1":
            clear()
            order.print_pizza(PIZZA_DICT)
            print()
        elif pizza_input == "2":
            clear()
            order.choose_pizza(PIZZA_DICT)
            clear()
        elif pizza_input == "3":
            counter = 0
            clear()
            order.remove_all_served(PIZZA_DICT)
            for i in PIZZA_DICT:
                counter += 1
            ID = counter
            print()
        elif pizza_input == "4":
            clear()
            order.print_pizza(PIZZA_DICT)
            print()
            ID += 1
            toping1 = input("Toping 1: ")
            toping2 = input("Toping 2: ")
            toping3 = input("Toping 3: ")
            new_pizza = Pizza(ID, toping1, toping2, toping3)
            new_pizza.add_pizza(PIZZA_DICT)
            print()
        elif pizza_input == "q":
            break
        else:
            print("Invalid input")
        print()

if __name__ == "__main__":
    main()
