class IndexOutOfBounds(Exception):
    pass
class Empty(Exception):
    pass

class ArrayList:
    def __init__(self):
        # TODO: remove 'pass' and implement functionality
        self.capacity = 16
        self.size = 0
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of list
    def __str__(self):
        # TODO: remove 'pass' and implement functionality
        return_string = ""
        for i in range(self.size):
            return_string += (str(self.arr[i]) + ", ")
        return return_string[:-2]

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        self.size += 1
        for i in range(self.size):
            self.arr[self.size - (i + 1)] = self.arr[self.size - (i + 2)]
        self.arr[0] = value

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # TODO: remove 'pass' and implement functionality
        self.size += 1
        if self.size < index:
            raise IndexOutOfBounds()

        for i in range(self.size):
            if index == (self.size - i):
                self.arr[self.size - (i + 1)] = value
                break
            else:
                self.arr[self.size - (i +  1)] = self.arr[self.size - (i + 2)]


    #Time complexity: O(1) - constant time
    def append(self, value):
        # TODO: remove 'pass' and implement functionality
        if self.size >= self.capacity:
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        if self.size < index:
            raise IndexOutOfBounds()
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        if self.size == 0:
            raise Empty()
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        if self.size < index:
            raise IndexOutOfBounds()
        return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        if self.size < 1:
            raise Empty()
        return self.arr[self.size-1]

    #Time complexity: O(n) - linear time in size of list
    def resize(self):
        # TODO: remove 'pass' and implement functionality
        index = 0
        self.capacity *= 2
        new_list = [0] * self.capacity
        for i in range(self.size):
            new_list[index] = self.arr[i]
            index += 1
        self.arr = new_list

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality

        if self.size <= index:
            raise IndexOutOfBounds()
        for i in range(self.size):
            if index == self.size:
                self.arr[self.size] = 0
                break
            if index == i:
                self.arr[i] = 0
            if index < i:
                self.arr[i - 1] = self.arr[i]
        self.size -= 1

    #Time complexity: O(1) - constant time
    def clear(self):
        # TODO: remove 'pass' and implement functionality
        self.capacity = 16
        self.size = 0
        self.arr = [0] * self.capacity

    #Time complexity: O(n) - linear time in size of sublist
    def sublist(self, start, length):
        # TODO: remove 'pass' and implement functionality
        index = 0
        new_list = [0] * length
        if start >= self.size:
            raise IndexOutOfBounds()
        for i in range(length):
            if self.arr[start+i] == 0:
                raise IndexOutOfBounds()
            new_list[index] = self.arr[start+i]
            index += 1
        return new_list


    #Time complexity: O(n) - linear time in size of concatinated list
    # OR
    #Time complexity: O(n+m) - linear time in size of both lists, self and other
    def concatenate(self, other):
        # TODO: remove 'pass' and implement functionality
        index = 0
        self.capacity = self.size + other.size
        new_list = [0] * self.capacity
        for i in range(self.size):
            new_list[index] = self.arr[i]
            index += 1
        for i in range(other.size):
            new_list[index] = other.arr[i]
            index += 1
        self.arr = new_list
        return self.arr
