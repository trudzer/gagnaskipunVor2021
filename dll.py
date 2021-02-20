
class Node:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DLL:
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

    def remove(self):
        ret_val = self.curr.data
        if self.header.next == self.trailer:
            return ret_val
        if self.curr.next == self.trailer:
            self.curr.prev.next = self.curr.next
            self.curr = self.curr.prev
            return ret_val

        self.curr.prev.next = self.curr.next
        self.curr = self.curr.next
        self.curr.prev = self.curr.prev.prev
        return ret_val

    def get_value(self):
        return self.curr.data

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

    def move_to_pos(self, pos):
        if self.header.next == self.trailer:
            return None
        temp = self.header
        self.curr = self.header.next
        counter = 0
        while temp.next != self.trailer:
            counter += 1
            temp = temp.next

        while counter != pos:
            counter -= 1
            self.curr = self.curr.next
        return self.curr.data

    def clear(self):
        self.header = Node(None, None, next)
        self.trailer = Node(self.header, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.curr = self.trailer

    def get_first_node(self):
        node = self.header.next
        if node == self.trailer:
            return None
        return node.data

    def get_last_node(self):
        node = self.trailer.prev
        if node == self.header:
            return None
        return node.data

    def partition(self, low, high):
        pass

    def sort(self):
        if self.header.next == self.trailer:
            return  None
        self.curr = self.header.next
        while self.curr.next != self.trailer:
            node = self.curr.next
            while node.next != self.trailer:
                if node.data > self.curr.data:
                    temp = self.curr.data
                    self.curr.data = node.data
                    node.data = temp
                node = node.next
            self.curr = self.curr.next
        self.curr = self.trailer.prev

    def __len__(self):
        counter = 0
        node = self.header.next
        while node != self.trailer:
            counter += 1
            node = node.next
        return counter

    def __str__(self):
        return_str = ""
        node = self.header.next
        while node != self.trailer:
            return_str += "{} ".format(node.data)
            node = node.next
        return return_str

if __name__ == "__main__":
    #create tests here if you want
    poslis = DLL()

    print("**********DLL Pos list**********\n")
    print("insert: ", end="")
    print(poslis.insert(1))
    print("insert: ", end="")
    print(poslis.insert(2))
    print("insert: ", end="")
    print(poslis.insert(3))
    print()
    print("The list: ", end="")
    print(poslis)
    print("size of list: ", end="")
    print(len(poslis))
    print("current position: ", end="")
    print(poslis.get_value())
    print("move to position ", end="")
    print(poslis.move_to_pos(1))
    print("current position: ", end="")
    print(poslis.get_value())
    print("insert: ", end="")
    print(poslis.insert(30))
    print("move to previous position")
    poslis.move_to_prev()
    print("insert: ", end="")
    print(poslis.insert(21))
    print("insert: ", end="")
    print(poslis.insert(15))
    print("insert: ", end="")
    print(poslis.insert(9))
    print("The list: ", end="")
    print(poslis)
    print("move to previous position")
    poslis.move_to_prev()
    print("current position: ", end="")
    print(poslis.get_value())
    print("remove: ",end="")
    print(poslis.remove())
    print()
    print("The list: ", end="")
    print(poslis)
    print()
    print("sort list:")
    poslis.sort()
    print()
    print("The list: ", end="")
    print(poslis)
    print()
    print("current position: ", end="")
    print(poslis.get_value())
    print("move to position ", end="")
    print(poslis.move_to_pos(3))
    print("insert: ", end="")
    print(poslis.insert(3))
    print()
    print("The list: ", end="")
    print(poslis)
    print()
    print("clear list:")
    poslis.clear()
    print()
    print("The list: ", end="")
    print(poslis)
    print("size of list: ", end="")
    print(len(poslis))
    print()
    print("insert: ", end="")
    print(poslis.insert(1))
    print("insert: ", end="")
    print(poslis.insert(2))
    print("move to next position")
    poslis.move_to_next()
    print("insert: ", end="")
    print(poslis.insert(3))
    print("move to previous position")
    poslis.move_to_prev()
    print("insert: ", end="")
    print(poslis.insert(4))
    print()
    print("The list: ", end="")
    print(poslis)
    print()
    print("current value: ", end="")
    print(poslis.get_value())
    print()
    print("The list: ", end="")
    print(poslis)
    print()
    print("size of list: ", end="")
    print(len(poslis))
    print("sort list:")
    poslis.sort()
    print()
    print("The list: ", end="")
    print(poslis)
    print()
    print("get first node: ", end="")
    print(poslis.get_first_node())
    print("get last node: ", end="")
    print(poslis.get_last_node())
    print("current value: ", end="")
    print(poslis.get_value())
    print("remove: ",end="")
    print(poslis.remove())
    print("The list: ", end="")
    print(poslis)
    print("remove: ",end="")
    print(poslis.remove())
    print("The list: ", end="")
    print(poslis)
    print("remove: ",end="")
    print(poslis.remove())
    print("The list: ", end="")
    print(poslis)
    print("remove: ",end="")
    print(poslis.remove())
    print("The list: ", end="")
    print(poslis)
    print("remove: ",end="")
    print(poslis.remove())
    print("The list: ", end="")
    print(poslis)
    print("sort list:")
    poslis.sort()
