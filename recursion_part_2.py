def string_recur(word):

    if word == "":
        return 0
    return string_recur(word[:-1]) + 1

print("Length of string:",end=" ")
print(string_recur('abcdefg'))


def linear_search(list, value):
    if list[::] == []:
        return False

    if list[-1] == value:
        return True

    return linear_search(list[:-1], value)

print("Value in list:", end=" ")
print(linear_search([1,2,3,4,5,"hallo"], "hallo"))



def count_instance(list, value, count):
    if list[::] == []:
        return count

    if list[-1] == value:
        count += 1
    return count_instance(list[:-1], value, count)

print("Number of instances:", end=" ")
print(count_instance([1,2,3,4,5,1,2,1,3,4,5],1,0))


def duplicate(list):
    for i in list[:-1]:
        if list[-1] == i:
            return True

    if len(list) == 0:
        return False

    return duplicate(list[:-1])

print("Duplicates:", end=" ")
print(duplicate([65,66,23,11,54,33,65,1,22,57]))


def remove_duplicate(list):
    if list[::] == []:
        return list

    head = list[0]
    tail = list[1:]
    
    if linear_search(tail, head):
        return remove_duplicate(tail)
    
    else:
        return [head] + remove_duplicate(tail)

print("list without duplicate:", end=" ")
print(remove_duplicate([1,2,3,4,1,2]))



def binary_search(list, value):
    if list[::] == []:
        return list

    index = list[len(list) // 2]

    if value in list:
        binary_search(list[index + 1:], value)
        return True

    if value in list:
        binary_search(list[:index - 1], value)
        return True

    else:
        return False

print("Binary search:", end=" ")
print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12], 10))