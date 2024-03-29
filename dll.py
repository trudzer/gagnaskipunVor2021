
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
            return None
        if self.curr.data == None:
            return None
        if self.curr.next == self.trailer:
            self.curr.prev.next = self.curr.next
            self.curr = self.curr.next
            return ret_val
        self.curr.prev.next = self.curr.next
        self.curr = self.curr.next
        self.curr.prev = self.curr.prev.prev
        return ret_val

    def get_value(self):
        return self.curr.data

    def move_to_next(self):
        if self.curr.next == self.trailer:
            self.curr = Node(self.trailer.prev, None, self.trailer)
            self.trailer.prev.next = self.curr
            self.trailer.prev = self.curr
            return self.curr.data
        else:
            self.curr = self.curr.next
            return self.curr.data

    def move_to_prev(self):
        if self.curr.prev == self.header:
            return None
        else:
            self.curr = self.curr.prev
            return self.curr.data

    def move_to_pos(self, pos):
        temp = self.header
        self.curr = self.header
        counter = 0
        while temp.next != None:
            counter += 1
            temp = temp.next
        for i in range(counter):
            self.curr = self.curr.next
            if i == pos:
                return self.curr.data

    def clear(self):
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.curr = self.trailer

    def get_first_node(self):
        node = self.header.next
        if node == self.trailer:
            return None
        return node

    def get_last_node(self):
        node = self.trailer.prev
        if node == self.header:
            return None
        return node

    def partition(self, low, high):
        if self.header.next == self.trailer:
            return None
        self.curr = self.header.next
        before = self.header.next
        after = self.header.next
        while self.curr.next != self.trailer:
            if self.curr.data < low.data:
                before.next = self.curr
                before = before.next
            else:
                after = self.curr
                after = after.next
            self.curr = self.curr.next
        while before.next != self.trailer:
            before.next = after.next
            after.next = self.trailer
        self.curr = self.header.next
        while self.curr.next != self.trailer:
            if self.curr.data == low.data:
                return self.curr
            self.curr = self.curr.next
        

    def sort(self):
        if self.header.next == self.trailer:
            return  None
        self.curr = self.header.next
        while self.curr.next != self.trailer:
            node = self.curr.next
            while node.next != None:
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
    pass
