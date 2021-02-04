def string_recur(strengur,teljari):
    if len(strengur) == 0:
        return
    teljari += 1
    print(teljari)
    string_recur(strengur[:-1], teljari)
    
#string_recur('ancdeyp',0)

def linear_search_recur(listi, index):
    if len(listi) == 0:
        return False
    if listi[-1] == index:
        return True
    return linear_search_recur(listi[:-1], index)

#print(linear_search_recur([62,'fab','ganga',69],'fab'))

def count_instance_recur(listi, index,counter):
    if len(listi) == 0:
        return counter
    if listi[-1] == index:
        counter += 1
    return count_instance_recur(listi[:-1], index, counter)

#print(count_instance_recur([32,32,65,78,35,32,11,1,12],32,0))

def duplicate_recur(listi):
    for i in listi[:-1]:
        if listi[-1] == i:
            return True
    if len(listi) == 0:
        return False
    return duplicate_recur(listi[:-1])

#print(duplicate_recur([65,66,23,11,54,33,65,1,22,57]))

def remove_duplicate(list):
    if len(list) <= 1:
        return list

    head = list[0]
    tail = list[1:]

    if linear_search_recur(tail, head):
        return remove_duplicate(tail)

    else:
        return [head] + remove_duplicate(tail)

#print("list without duplicate:", end=" ")
#print(remove_duplicate([1,2,3,4,1,2]))

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

print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12], 10))
