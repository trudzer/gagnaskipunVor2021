class Node:

    def __init__(self,data = None, next = None):
        self.data = data
        self.next = next

def print_nodes(head):
    node = head
    while node != None:
        print(node.data, end=" ")
        node = node.next
    print()

def counter_iterative(head):
    node = head
    counter = 0
    while node != None:
        counter += 1
        node = node.next
    return counter

def print_recursive(head):
    node = head
    if node == None:
        return None
    else:
        print(node.data, end=" ")
    return print_recursive(node.next)

def counter_recursive(head):
    node = head
    counter = 0
    return counter_helper(node, counter)

def counter_helper(node, counter):
    if node == None:
        return counter
    counter += 1
    return counter_helper(node.next, counter)

def linear_search(head, value):
        if head == None:
            return False
        if value == head.data:
            return True
        return linear_search(head.next, value)

def delete_every_other(head):
    return deo_helper(head, 0)

def deo_helper(head, i):
    if head == None:
        return None
    if i % 2 == 1:
        head.next = deo_helper(head.next, i+1)
        return head
    else:
        return deo_helper(head.next, i+1)

def merge_list(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1.data <= head2.data:
        head1.next = merge_list(head1.next, head2)
        return head1
    else:
        head2.next = merge_list(head1, head2.next)
        return head2

def insert_list(head, value):
    if head == None:
        head = Node(value, None)
        return head
    if head.data == None:
        head = Node(value, None)
        return head
    if value > head.data:
        head.next = insert_list(head.next, value)
        return head
    if value <= head.data:
        head.next = Node(head.data, head.next)
        head.data = value
        return head

def reverse_list(head):
    prev = None
    temp = head
    while temp != None:
        next = temp.next
        temp.next = prev
        prev = temp
        temp = next
    head = prev
    return head

def merge_sort(head):
    node = head
    temp1 = Node(head.data, None)
    temp2 = Node(head.next.data, None)
    new_linked_list = merge_list(temp1, temp2)
    while node != None:
        node = node.next
        if node.next == None:
            break
        temp1 = Node(node.next.data, None)
        new_linked_list = merge_list(new_linked_list, temp1)
    return new_linked_list

head = Node(1, Node(3, Node(5, Node(7, Node(9, Node(11, Node(13, None)))))))
head2 = Node(2, Node(4, Node(6, Node(8, Node(10, Node(12, Node(14, None)))))))
head3 = Node(111, Node(113, Node(115, Node(117, Node(119, Node(1111, Node(1113, None)))))))
head4 = Node(31, Node(32, Node(33, Node(34, Node(35, Node(36, Node(37, None)))))))
head5 = Node(7, Node(3, Node(4, Node(1, Node(6, Node(2, Node(5, None)))))))

head5 =  merge_sort(head5)
print("merge sort: ", end="")
print_nodes(head5)

print()
head4 = reverse_list(head4)
print("reverse list: ", end="")
print_nodes(head4)

print()
head = insert_list(head, 15)
print("insert into list: ", end="")
print_nodes(head)

print()
print("iterative counter: ", end="")
print(counter_iterative(head))

print()
print("recursive counter: ", end="")
print(counter_recursive(head))

print()
print("recursive: ", end="")
print_recursive(head)

print()
print()
print("iterative: ", end="")
print_nodes(head)

print()
print("iterative: ", end="")
print_nodes(head2)

print()
print("linear search: ", end="")
print(linear_search(head, 3))

print()
print("iterative: ", end="")
print_nodes(head3)

print()
print("delete every other: ", end="")
print_nodes(delete_every_other(head3))

lis = merge_list(head,head2)
print()
print("merge list: ", end="")
print_nodes(lis)

print()
print("merge list: ", end="")
lis = merge_list(lis, head3)
print_nodes(lis)

print()
head = Node()
print("list cleared: ", end="")
print_nodes(head)
print()
head = insert_list(head, 20)
head = insert_list(head, 21)
head = insert_list(head, 22)
head = insert_list(head, 23)
print("insert into list: ", end="")
print_nodes(head)
