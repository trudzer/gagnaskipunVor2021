def string_recur(word):

    if word == "":
        return 0
    return string_recur(word[:-1]) + 1


def linear_search(list, value):
    if list[::] == []:
        return False

    if list[-1] == value:
        return True

    return linear_search(list[:-1], value)


def count_instance(list, value):
    if list[::] == []:
        return 0

    if list[-1] == value:
        return count_instance(list[:-1], value) + 1
    
    return count_instance(list[:-1], value)


def duplicate(list):
    for i in list[:-1]:
        if list[-1] == i:
            return True

    if len(list) == 0:
        return False

    return duplicate(list[:-1])


def remove_duplicate(list):
    if list[::] == []:
        return list

    head = list[0]
    tail = list[1:]
    
    if linear_search(tail, head):
        return remove_duplicate(tail)
    
    else:
        return sorted([head] + remove_duplicate(tail))


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


print("Length of string:",end=" "), print(string_recur('abcdefghijklmn'))
print("Value in list:", end=" "), print(linear_search([1,2,3,4,5,"hallo",6,7,9], "hallo"))
print("Number of instances:", end=" "), print(count_instance([1,2,3,4,5,1,2,1,3,4,5,1,2,1,1,1],1))
print("Duplicates:", end=" "), print(duplicate([65,66,23,11,54,33,65,1,22,57]))
print("list without duplicate:", end=" "), print(remove_duplicate([1,2,3,4,1,2,5,6,7,5,6,3,8,9,10,11,11,4]))
print("Binary search:", end=" "), print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18], 10))