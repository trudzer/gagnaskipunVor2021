class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            self._add(key, self.root)

    def _add(self, key, curr_node):
        if key < curr_node.val:
            if curr_node.left == None:
                curr_node.left = Node(key)
            else:
                self._add(key, curr_node.left)
        elif key > curr_node.val:
            if curr_node.right == None:
                curr_node.right = Node(key)
            else:
                self._add(key, curr_node.right)
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

    def contains(self,key):
        if self.root != None:
            return self._contains(key, self.root)
        else:
            return False

    def _contains(self, key, curr_node):
        if key == curr_node.val:
            print("\n[TRUE] The key {} is in the tree".format(key))
            return True
        elif key < curr_node.val and curr_node.left != None:
            return self._contains(key, curr_node.left)
        elif key > curr_node.val and curr_node.right != None:
            return self._contains(key, curr_node.right)
        print("\n[FALSE] The key {} is not in the tree".format(key))
        return False 

    def __len__(self):
        if self.root != None:
            return self._size(self.root)
        else:
            return 0

    def _size(self,node):
        if node is None: 
            return 0 
        else: 
            return (self._size(node.left)+ 1 + self._size(node.right)) 
 
r = BST()
r.add(5)
r.add(3)
r.add(2)
r.add(4)
r.add(7)
r.add(6)
r.add(8)
r.add(9)
r.add(1)
r.add(11)
r.add(16)
r.add(13)
r.add(19)
r.add(20)
r.add(17)
r.add(12)


r.print_tree()

r.contains(6)
r.contains(666)

print("\nThe size of the tree is:", end=" ")
print(len(r))
