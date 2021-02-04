class Deque:

    DEFAULT_CAPACITY = 4
    DEFAULT_SIZE = 0
    DEFAULT_ARRAY = [0] * DEFAULT_CAPACITY

    def __init__(self):
        self.capacity = Deque.DEFAULT_CAPACITY
        self.size = Deque.DEFAULT_SIZE
        self.arr = Deque.DEFAULT_ARRAY

    def __str__(self):
        return_string = ""
        the_str = "the list: "
        for i in range(self.size):
            return_string += "{}, ".format(str(self.arr[i]))
        the_str +=  return_string[:-2]
        return the_str

    def __is_empty(self):
        print("List is empty!")

    def resize(self):
        index = 0
        self.capacity *= 2
        new_list = [0] * self.capacity
        for i in range(self.size):
            new_list[index] = self.arr[i]
            index += 1
        self.arr = new_list

    def clear(self):
        self.capacity = Deque.DEFAULT_CAPACITY
        self.size = Deque.DEFAULT_SIZE
        self.arr = Deque.DEFAULT_ARRAY
        print("\nList is cleared!\n")

    def push_back(self, value):
        if self.size >= self.capacity:
            self.resize()
        i = self.size
        while(i > 0):
            self.arr[i] = self.arr[i - 1]
            i -= 1
        self.arr[0] = value
        self.size += 1
        print("{:<9} pushed back".format(self.arr[0]))

    def push_front(self, value):
        if self.size >= self.capacity:
            self.resize()
        self.size += 1
        self.arr[self.size-1] = value
        print("{:<9} pushed infront".format(self.arr[self.size-1]))

    def pop_front(self):
        if self.size == 0:
            print("Cannot pop front. ", end="")
            self.__is_empty()
            return 0
        else:
            last_num =  self.arr[self.size-1]
            self.arr[self.size-1] = 0
            self.size -= 1
            print("{:<9} removed from front".format(last_num))
            return last_num

    def pop_back(self):
        if self.size == 0:
            print("Cannot pop back. ", end="")
            self.__is_empty()
            return 0
        else:
            first_num = self.arr[0]
            size = self.size
            i = 0
            while(i < size):
                self.arr[i] = self.arr[i + 1]
                i += 1
            self.size -= 1
            print("{:<9} removed from back".format(first_num))
            return first_num


stack_lis = Deque()

stack_lis.push_front(3)
stack_lis.push_front(2)
stack_lis.push_back(4)
stack_lis.push_back(5)
stack_lis.push_back(6)
stack_lis.push_front(1)

print("-"*40)
print(str(stack_lis))
print("-"*40)

stack_lis.pop_front()
stack_lis.pop_back()
stack_lis.pop_front()
stack_lis.pop_back()

print("-"*40)
print(str(stack_lis))
print("-"*40)

stack_lis.clear()

print("-"*40)
print(str(stack_lis))
print("-"*40)

stack_lis.pop_front()
stack_lis.pop_back()
