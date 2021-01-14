def power(n,power):
    if n == 0 and exp == 0:
        raise Exception("0 to the power of 0 is undefined")
    total = 1
    for i in range(power):
        total *= n
    return total

def multiply(a,b):
    total = 0
    for i in range(a):
        total += b
    return total

def random_number(size):
    list = [0] * size
    for i in range(size):
        list[i] = random.randint(1,32)
    return list

def print_list(list):
    list_str = ""
    for i in list:
        list_str += str(i) + ",\t"
    list_str = list_str[:-2]
    print(list_str)

def increase(list):
    index = random.randint(1, len(list)-1)
    list[index] = list[index] + 1
    return list

def switch(list, index):
    list[index], list[index+1] = list[index+1], list[index]
    return list

def rand_switch(list):
    index1 = random.randint(0, len(list)-1)
    index2 = random.randint(0, len(list)-1)
    temp = list[index1]
    list[index1] = list[index2]
    list[index2] = temp
    return list
    
    
print("power:",power(2,4))
print("multiply:",multiply(5,6))
the_list = random_number(9)
print("list: ", end="\t\t")
print_list(the_list)

increase(the_list)
print("increase:", end="\t")
print_list(the_list)

switch(the_list, 2)
print("switch:", end="\t\t")
print_list(the_list)

rand_switch(the_list)
print("random switch:", end="\t")
print_list(the_list)
