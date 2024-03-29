def less_than(a, b):  # ONLY NEEDS TO WORK FOR POSITIVE INTEGERS
    #TODO: remove 'pass' and implement functionality
    if a == b:
        return False
    if (a%b) == a:
        return True
    if (a%b) == 0:
        return False
    return less_than(a,(a%b))


def unique(lis1):
    #TODO: remove 'pass' and implement functionality
    if lis1 == []:
        return lis1

    head = lis1[0]
    tail = lis1[1:]
    
    if unique_help(tail, head):
        return unique(tail)
    
    else:
        return sorted([head] + unique(tail))

def unique_help(lis1, value):
    if lis1 == []:
        return False

    if lis1[-1] == value:
        return True

    return unique_help(lis1[:-1], value)


# FEEL FREE TO EDIT THE TESTS AND MAKE THEM BETTER
# REMEMBER EDGE CASES!

def test_less_than(num1, num2):
    if(less_than(num1, num2)):
        print(str(num1) + " is less than " + str(num2))
    else:
        print(str(num1) + " is NOT less than " + str(num2))

def test_unique(lis1):
    print(str(unique(lis1)) + " are the unique items in " + str(lis1))

def run_recursion_program():

    print("\nTESTING LESS THAN:\n")

    test_less_than(8, 3)
    test_less_than(2, 9)
    test_less_than(4, 17)
    test_less_than(11, 3)
    test_less_than(8, 2)
    test_less_than(8, 7)
    test_less_than(7, 8)
    test_less_than(6, 16)
    test_less_than(7, 7)

    print("\nTESTING UNIQUE:\n")

    test_unique(['a', 'f', 'd', 't', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['a', 'b', 'f', 'g', 'a', 't', 'c', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['f', 'g', 't', 'a', 'b', 'c', 'd', 'e'])
    test_unique(['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'])
    test_unique(['t'])


if __name__ == "__main__":
    run_recursion_program()
