class pizza:
    pizzas = {}
    c = 0
    pizza_list = []
    def __init__(self, topping1 = None, topping2 = None, topping3 = None):
        self.pizzas = {self.c: (topping1, topping2, topping3, 'unserved')}
        for i in self.pizzas:
            self.pizza_list.append([])
            self.pizza_list[i].append(str(i))
            for b in self.pizzas[i]:
                self.pizza_list[i].append(b)
        

    def make_served(self, ID):
        self.pizzas[ID][3] = 'served'
    
    def __str__(self):
        new_list = []
        for i in self.pizza_list:
            for b in i:
                new_list.append(b)
            new_list.append('\n')
        return ' '.join(new_list)
    
for i in range(3):       
    pizza1 = pizza('pepperoni', 'ham', 'extra cheese')
print(pizza1)

