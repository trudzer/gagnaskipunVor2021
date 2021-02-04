class Stack:

    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity
    
    def __str__(self):
        return_string = ""
        for i in range(self.size):
            return_string += str(self.arr[i])
            return_string += ', '
        return return_string[:-2]

    def push(self, value):
        if self.size == self.capacity:
            self.resize()
        self.size += 1
        self.arr[self.size-1] = value
        
    def pop(self):
        last_num = self.arr[self.size-1]
        self.arr[self.size-1] = 0
        self.size -= 1
        print("{:<8} removed from front".format(last_num))
        return last_num

    def resize(self):
        self.capacity *= 2
        index = 0
        temp = [0] * self.capacity
        for i in range(self.size):
            temp[index] = self.arr[i]
            index += 1
        self.arr = temp

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()
print(str(stack))

class Queue:

    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity

    def __str__(self):
        return_string = ""
        for i in range(self.size):
            return_string += str(self.arr[i])
            return_string += ', '
        return return_string[:-2]
    
    def add(self, value):
        if self.size == self.capacity:
            self.resize()
        self.size += 1
        for i in range(self.size):
            self.arr[self.size-(i+1)] = self.arr[self.size - (i+2)]
        self.arr[0] = value
    
    def remove(self):
        first_num = self.arr[0]
        for i in range(self.size):
            self.arr[i] = self.arr[i +1]
        self.size -= 1
        print('{:<8} removed from back'.format(first_num))
        return first_num
    
    def resize(self):
        self.capacity *= 2
        index = 0
        temp = [0] * self.capacity
        for i in range(self.size):
            temp[index] = self.arr[i]
            index += 1
        self.arr = temp
    
que = Queue()
que.add(5)
que.add(4)
que.add(3)
que.add(2)
que.add(1)
que.remove()
print(str(que))

class Deque:

    def __init__(self):
        self.capacity = 4
        self.size = 0
        self.arr = [0] * self.capacity

    def __str__(self):
        return_string = ""
        for i in range(self.size):
            return_string += str(self.arr[i])
            return_string += ', '
        return return_string[:-2]
    
    def resize(self):
        self.capacity *= 2
        index = 0
        temp = [0] * self.capacity
        for i in range(self.size):
            temp[index] = self.arr[i]
            index += 1
        self.arr = temp
    
    def push_front(self, value):
        if self.size == self.capacity:
            self.resize()
        self.size += 1
        self.arr[self.size-1] = value

    def push_back(self, value):
        if self.size == self.capacity:
            self.resize()
        self.size += 1
        for i in range(self.size):
            self.arr[self.size-(i+1)] = self.arr[self.size - (i+2)]
        self.arr[0] = value

    def pop_front(self):
        last_num = self.arr[self.size-1]
        self.arr[self.size-1] = 0
        self.size -= 1
        print("{:<8} removed from front".format(last_num))
        return last_num

    def pop_back(self):
        first_num = self.arr[0]
        for i in range(self.size):
            self.arr[i] = self.arr[i +1]
        self.size -= 1
        print('{:<8} removed from back'.format(first_num))
        return first_num

    