class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)

    def _insert(self, key, curr_node):
        if key < curr_node.val:
            if curr_node.left == None:
                curr_node.left = Node(key)
            else:
                self._insert(key, curr_node.left)
        elif key > curr_node.val:
            if curr_node.right == None:
                curr_node.right = Node(key)
            else:
                self._insert(key, curr_node.right)
        else:
            print("key already in tree!")

    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)

    def _print_tree(self, curr_node):
        if curr_node != None:
            self._print_tree(curr_node.left)
            print(curr_node.val)
            self._print_tree(curr_node.right)

    def search(self,key):
        if self.root != None:
            return self._search(key, self.root)
        else:
            return False

    def _search(self, key, curr_node):
        if key == curr_node.val:
            print("The key {} is in the list".format(key))
            return True
        elif key < curr_node.val and curr_node.left != None:
            return self._search(key, curr_node.left)
        elif key > curr_node.val and curr_node.right != None:
            return self._search(key, curr_node.right)
        print("The key {} is not in the list".format(key))
        return False 
 
r = BST()
r.insert(50)
r.insert(30)
r.insert(20)
r.insert(40)
r.insert(70)
r.insert(60)
r.insert(80)
r.insert(90)

r.print_tree()

r.search(60)