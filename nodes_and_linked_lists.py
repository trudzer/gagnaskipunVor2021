class Node:

    def __init__(self, data, next):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None


    def add_to_front(self, data):
        self.head = Node(data, self.head)
        if self.tail == None:
            self.tail = self.head


    def add_to_back(self, data):
        #new_node = self.head
        #while (new_node.next != None):
        #    new_node = new_node.next
        #new_node.next = Node(data, None)
        self.tail.next = Node(data, None)
        self.tail = self.tail.next
        if self.head == None:
            self.head = self.tail

    def remove_front(self):
        if self.head != None:
            ret_val = self.head.data
            self.head = self.head.next
            return ret_val
        else:
            print("List is already empty!")

    def remove_back(self):
        node = self.head
        while node.next.next != None:
            node = node.next
        node.next = None

    def print_node(self):
        node = self.head
        return_str = ""
        while node != None:
            return_str += "{} - ".format(node.data)
            node = node.next
        print(return_str[:-2])

lis = LinkedList()

lis.add_to_front(44)
lis.add_to_front(2)
lis.add_to_back(3)
lis.add_to_front(1)
lis.add_to_back(4)
lis.add_to_back(5)
lis.remove_back()
lis.remove_front()
lis.print_node()
