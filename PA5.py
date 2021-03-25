class ItemExistsException(Exception):
    pass

class NotFoundException(Exception):
    pass

class Node:

    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

class Bucket:

    def __init__(self):
        self.head = None
        self.curr = None

    def insert(self, key, value):
        node = self.head
        if self.head == None:
            self.head = Node(key, value, None)
            self.curr = self.head
            return
        if self.head.next == None:
            self.head.next = Node(key, value, None)
            self.curr = self.head.next
            return
        self.insert_helper(node, key, value)
    
    def insert_helper(self, node, key, value):
        if node.next == None:
            node.next = Node(key, value, None)
            self.curr = node.next
            return
        if node.key == key:
            raise ItemExistsException()
        else:
            self.insert_helper(node.next, key, value)
    
    def remove(self, key):
        node = self.head 
        if node != None: 
            if node.key == key: 
                self.head = node.next
                node = None
                return 
        while node != None: 
            if node.key == key: 
                break
            prev = node 
            node = node.next
            self.curr = node
        if node == None:
            raise NotFoundException()
        prev.next = node.next
        node = None
                

    def find(self, key):
        if self.head.next == None:
            return None
        node = self.head
        while node.next != None:
            if node.key == key:
                self.curr = node
                return node
            node = node.next
        raise NotFoundException()

    def update(self, key, value):
        node = self.head
        while node != None:
            if node.key == key:
                node.value = value
                self.curr = node
                return
            node = node.next
            self.curr = node
        raise NotFoundException()

    def contains(self, key):
        node = self.head
        while node != None:
            if node.key == key:
                return True
            node = node.next
        return False

    def __setitem__(self, key, value):
        node = self.head
        boolean = self.contains(key)
        if boolean == True:
            while node != None:
                if node.key == key:
                    node.value = value
                    return
                node = node.next
        else:
            self.insert(key, value) 

    def __getitem__(self, key):
        node = self.head
        boolean = self.contains(key)
        if boolean == True:
            while node != None:
                if node.key == key:
                    return node.value
                node = node.next
        else:
            raise NotFoundException()

    def __len__(self):
        counter = 0
        node = self.head
        while node != None:
            counter += 1
            node = node.next
        return counter

    def __str__(self):
        node = self.head
        return_str = "output: "
        while node != None:
            return_str += "{" + str(node) + "} "
            node = node.next
        return return_str


class HashMap:
    def __init__(self):
        self.capacity = 8
        self.bucket_list = []
        self.size = 0

        for i in range(self.capacity):
            self.bucket_list.append([])

    def rebuild(self):
        for i in range(self.capacity):
            self.bucket_list.append([])
        self.capacity *= 2

    def __hashing(self, key):
        return hash(key) % self.capacity

    def insert(self, key, data):
        if self.size >= (self.capacity * 1.2):
            self.rebuild()
        value = self.__hashing(key)
        values = {key: data}
        if self.bucket_list[value] == None:
            self.bucket_list[value].append(values)
        else:
            if self.contains(key):
                raise ItemExistsException()
            self.bucket_list[value].append(values)
            self.size += 1

    def contains(self, key):
        for i in self.bucket_list:
            for b in i:
                if key in b.keys():
                    return True
        else:
            return False

    def update(self, key, data):
        if self.contains(key):
            for i in self.bucket_list:
                for b in i:
                    if key in b.keys():
                        b[key] = data
                        return
        else:
            raise NotFoundException()

    def find(self, key):
        value = self.__hashing(key)
        if self.contains(key) == False:
            raise NotFoundException()
        for i in self.bucket_list:
                for b in i:
                    if key in b.keys():
                        return b[key]

    def __getitem__(self, key):
        value = self.__hashing(key)
        if self.contains(key):
            for i in self.bucket_list:
                for b in i:
                    if key in b.keys():
                        return b[key]
        return "get item for {} not found".format(key)
        raise NotFoundException()

    def __setitem__(self, key, data):
        boolean = self.contains(key)
        if boolean == True:
            self.update(key, data)
        else:
            self.insert(key, data)

    def remove(self, key):
        counter = 0
        counter2 = 0
        if self.contains(key):
            for i in self.bucket_list:
                for b in i:
                    if key in b.keys():
                        self.bucket_list[counter].pop(counter2)
                        self.size -= 1
                        return
                    counter2 += 1
                counter += 1
                counter2 = 0
        else:
            raise NotFoundException()

    def __str__(self):
        return_str = "output: "
        for i in self.bucket_list:
            for j in i:
                if i != [] and j != [] and len(str(j)):
                    return_str += "{} ".format(str(j))
        return return_str

    def __len__(self):
        return self.size


class MyHashableKey:
    
    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value
        self.value = None

    def __hash__(self):
        hash_code = 0
        string_hash = ""
        for i in range(len(self.string_value)):
            hash_code += ord(self.string_value[i]) * (2**i)
        string_hash = (len(self.string_value) * hash_code)
        self.value = (self.int_value + string_hash) % 16
        return self.value

    def __str__(self):
        return "{}:{}".format(self.int_value, self.string_value)

    def __eq__(self, other):
        if self.value == other.value:
            return True
        else:
            return False
