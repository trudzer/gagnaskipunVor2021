class Error(Exception):
    pass
class ItemExistsException(Error):
    pass
class NotFoundException(Error):
    pass
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.key) + ":" + str(self.value)

class BSTMap(object):
    def __init__(self):
        self.root = None
        self.size = 0
        self.listi = []

    def __len__(self):
        return self.size
    def contains(self,key):
        return not self.findNode(self.root,key) is None
    def __getitem__(self,key):
        node = self.findNode(self.root, key)
        if node == None:
            raise NotFoundException()
        return node.value
    def find(self,key):
        return self[key]

    def findNode(self, subtree, key):
        
        if subtree == None:
            return None
        elif subtree.key == key:
            return subtree
        elif subtree.key < key:
            return self.findNode(subtree.right, key)
        else:
            return self.findNode(subtree.left, key)

    def update(self,key,value):
        node = self.findNode(self.root, key)
        if node == None:
            raise NotFoundException()
        self[key]=value
        
    def __setitem__(self, key, value):
       
        if self.root == None:
            self.root = Node(key, value)
            self.size += 1
        else:
            self.setItem(self.root, key, value)
    def setItem(self, subtree, key, value):
        assert subtree is not None
        if subtree.key == key:
            subtree.value = value
        elif key < subtree.key:
            if subtree.left is None:
                subtree.left = Node(key, value)
                self.size += 1
            else:
                self.setItem(subtree.left, key, value)
        else:
            if subtree.right is None:
                subtree.right = Node(key, value)
                self.size += 1
            else:
                self.setItem(subtree.right, key, value)

    def insert(self,key,value):
        if self.root == None:
            self.root = Node(key, value)
            self.size += 1
        else:
            self.insertItem(self.root, key, value)
    def insertItem(self,subtree,key,value):
        assert subtree is not None
        if subtree.key == key:
            raise ItemExistsException() 
        elif key < subtree.key:
            if subtree.left is None:
                subtree.left = Node(key, value)
                self.size += 1
            else:
                self.insertItem(subtree.left, key, value)
        else:
            if subtree.right is None:
                subtree.right = Node(key, value)
                self.size += 1
            else:
                self.insertItem(subtree.right, key, value)

    def __str__(self):
        return_string = "output: "
        if self.root != None:
            self._print_tree(self.root)
        for i in self.listi:
            return_string += "{" + str(i) + "} "
        self.listi = []
        return return_string


    def _print_tree(self, curr_node):
        if curr_node != None:
            self._print_tree(curr_node.left)
            self.listi.append(curr_node)
            self._print_tree(curr_node.right)

        
    def remove(self, key):
        value = self[key]
        self.root = self.bstRemove(self.root, key)
        self.size -= 1
        return value

    def bstRemove(self, subtree, key):
        assert subtree is not None #
        if key < subtree.key:
            subtree.left = self.bstRemove(subtree.left, key)
            return subtree
    
        elif key > subtree.key:
            subtree.right = self.bstRemove(subtree.right, key)
            return subtree
        else:
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is not None and subtree.right is None:
                return subtree.left
            elif subtree.left is None and subtree.right is not None:
                return subtree.right
            else:
                successor = self.bstMinimum(subtree.right)
                subtree.key = successor.key
                subtree.value = successor.value
                subtree.right = self.bstRemove(subtree.right, successor.key)
                return subtree
    def bstMinimum(self, subtree):
        if subtree is None:
            return None
        if subtree.left is None:
            return subtree
        else:
            return self.bstMinimum(subtree.left)


class MyComparableKey:

    def __init__(self, int_value, string_value):
        self.int_value = int_value
        self.string_value = string_value
        self.node = Node(int_value, string_value)

    def __lt__(self, other):
        if self.node.key < other.node.key:
            return True
        if self.node.key == other.node.key:
            if self.node.value < other.node.value:
                return True
            else:
                return False
            return True
        else:
            return False