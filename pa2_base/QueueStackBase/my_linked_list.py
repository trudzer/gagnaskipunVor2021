class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push_front(self, data):
        self.head = Node(data, self.head)
        if self.tail == None:
            self.tail = self.head
    
    def pop_front(self):
        if self.head == None:
            return None
        if self.head.next != None:
            ret_val = self.head.data
            self.head = self.head.next
            return ret_val
        else:
            self.head = self.head.next
            return None
    
    def push_back(self, data):
        node = Node(data, None)
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def pop_back(self):
        node = self.head
        if self.head == None:
            return None
        if self.head.next == None:
            ret_val = self.head.data
            self.head = None
            return ret_val
        while node.next.next != None:
            node = node.next
        ret_val = self.tail.data
        self.tail = node
        self.tail.next = None
        return ret_val


    def get_size(self):
        counter = 0
        node = self.head
        while node != None:
            counter  += 1
            node = node.next
        return counter

    def __str__(self):
        node = self.head
        return_str = ""
        while node != None:
            return_str += "{} ".format(node.data)
            node = node.next
        return return_str
