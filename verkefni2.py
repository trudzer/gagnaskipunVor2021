import random
def power(base, exp):
    if (base == 0 and exp == 0):
        raise Exception("0 to the power of 0 is undefiend")
    retVal = 1
    for i in range(exp):
        retVal *= base
    print(retVal)
    return retVal



def multiplication(a,b):
    if b > a:
        temp = b
        b = a
        b = temp
    counter = 0
    for i in range(b):
        counter += a
    print(counter)
    return counter


def random_list(size):
    listi = [0] * size
    for i in range(size):
        listi[i] = random.randint(1,6)
    return listi

def print_list(listin):
    for i in listin[0:-1]:
        print(str(i) + ", ", end='')
    print(listin[-1])

b = random_list()
print_list(b)

def insert_ordered(listi, value):
    listi.append(3)
    i = len(listi-1)
    while True:
        if i == 0:
            break
        if listi[i] > listi[i-1]:
            break
        temp = listi[i]
        listi[i] = listi[i-1]
        listi[i-1] = temp
        i -= 1