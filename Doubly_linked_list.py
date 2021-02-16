class Node:

    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next



class DoublyLinkedList:

    def __init__(self):
        self.header = Node(None, None, next)
        self.trailer = Node(self.header, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def __str__(self):
        return_str = ""
        node = self.header.next
        while node != self.trailer:
            return_str += "{} ".format(node.data)
            node = node.next
        return return_str

    def push_front(self, data):
        node = Node(self.header, data, self.header.next)
        self.header.next.prev = node
        self.header.next = node
        return node.data


    def push_back(self, data):
        node = Node(self.trailer.prev, data, self.trailer)
        self.trailer.prev.next = node
        self.trailer.prev = node
        return node.data

    def pop_front(self):
        if self.header.next == self.trailer:
            return None
        ret_node = self.header.next
        ret_node.next.prev = self.header
        self.header.next = self.header.next.next
        return ret_node.data

    def pop_back(self):
        if self.trailer.prev == self.header:
            return None
        ret_node = self.trailer.prev
        ret_node.prev.next = self.trailer
        self.trailer.prev = self.trailer.prev.prev
        return ret_node.data



class DLL_PosList:

    def __init__(self):
        self.header = Node(None, None, next)
        self.trailer = Node(self.header, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.curr = self.trailer

    def insert(self, data):
        node = Node(self.header, data, self.header.next)
        if self.curr.prev == None:
            self.curr = node
        node.next = self.curr
        node.prev = self.curr.prev
        self.curr.prev.next = node
        self.curr.prev = node
        self.curr = node
        return node.data

    def move_to_next(self):
        if self.curr.next == None:
            return self.curr.data
        self.curr = self.curr.next
        return self.curr.data

    def move_to_prev(self):
        if self.curr.prev == None:
            return self.curr.data
        self.curr = self.curr.prev
        return self.curr.data

    def __str__(self):
        return_str = ""
        node = self.header.next
        while node != self.trailer:
            return_str += "{} ".format(node.data)
            node = node.next
        return return_str

    def print_backwards(self):
        return_str = ""
        node = self.trailer.prev
        while node != self.header:
            return_str += "{} ".format(node.data)
            node = node.prev
        return return_str

    def get_size(self):
        counter = 0
        node = self.header.next
        while node != self.trailer:
            counter += 1
            node = node.next
        return counter

    def get_value(self):
        return self.curr.data

    def remove(self):
        if self.curr.next == None:
            return None
        ret_val = self.curr.data
        self.curr.prev.next = self.curr.next
        self.curr = self.curr.next
        self.curr.prev = self.curr.prev.prev
        return ret_val

    def update(self, data):
        self.curr.data = data
        return self.curr.data



if __name__ == "__main__":

    dll = DoublyLinkedList()

    print("**********Doubly Linked List**********")
    print()
    print("push front:\t", end="")
    print(dll.push_front(4))
    print("push front:\t", end="")
    print(dll.push_front(3))
    print("push front:\t", end="")
    print(dll.push_front(2))
    print("push front:\t", end="")
    print(dll.push_front(1))
    print("push back:\t", end="")
    print(dll.push_back(5))
    print("push back:\t", end="")
    print(dll.push_back(6))
    print("push back:\t", end="")
    print(dll.push_back(7))
    print()
    print("List:\t\t", end="")
    print(dll)
    print()
    print("pop front:\t", end="")
    print(dll.pop_front())
    print("pop front:\t", end="")
    print(dll.pop_front())
    print("pop front:\t", end="")
    print(dll.pop_front())
    print("List:\t\t", end="")
    print()
    print(dll)
    print()
    print("pop back:\t", end="")
    print(dll.pop_back())
    print("pop back:\t", end="")
    print(dll.pop_back())
    print()
    print("List:\t\t", end="")
    print(dll)
    print()

    

    poslis = DLL_PosList()
    poslis2 = DLL_PosList()

    print("**********DLL Pos list**********\n")
    print("insert: ", end="")
    print(poslis.insert('A'))
    print("insert: ", end="")
    print(poslis.insert('B'))
    print("insert: ", end="")
    print(poslis.insert('C'))
    print()
    print("The list: ", end="")
    print(poslis)
    print("size of list: ", end="")
    print(poslis.get_size())
    print("list backwards: ", end="")
    print(poslis.print_backwards())
    print()
    print("insert: ", end="")
    print(poslis2.insert('A'))
    print("insert: ", end="")
    print(poslis2.insert('B'))
    print("move to next position")
    poslis2.move_to_next()
    print("insert: ", end="")
    print(poslis2.insert('C'))
    print("move to previous position")
    poslis2.move_to_prev()
    print("insert: ", end="")
    print(poslis2.insert('D'))
    print()
    print("The list: ", end="")
    print(poslis2)
    print()
    print("current value: ", end="")
    print(poslis2.get_value())
    print("update value: ", end="")
    print(poslis2.update('X'))
    print()
    print("The list: ", end="")
    print(poslis2)
    print()
    print("size of list: ", end="")
    print(poslis2.get_size())
    print("list backwards: ", end="")
    print(poslis2.print_backwards())
    print()
    print("remove: ",end="")
    print(poslis2.remove())
    print("The list: ", end="")
    print(poslis2)
    print("remove: ",end="")
    print(poslis2.remove())
    print("The list: ", end="")
    print(poslis2)
    print("remove: ",end="")
    print(poslis2.remove())
    print("The list: ", end="")
    print(poslis2)
    print("remove: ",end="")
    print(poslis2.remove())
    print("The list: ", end="")
    print(poslis2)
    print("remove: ",end="")
    print(poslis2.remove())
    print("The list: ", end="")
    print(poslis2)
