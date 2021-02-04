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
            return_string += str(self.arr[i])
            return_string += ', '
        return return_string[:-2]

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        if self.size == self.capacity:
            self.resize()
        self.size += 1
        for i in range(self.size):
            self.arr[self.size-(i+1)] = self.arr[self.size - (i+2)]
        self.arr[0] = value
        

    #Time complexity: O(n) - linear time in size of list
    def insert(self, value, index):
        # TODO: remove 'pass' and implement functionality
        if self.size == self.capacity:
            self.resize()
        if (self.size + 1) <= index or index < 0:
            raise IndexOutOfBounds()
        self.size += 1
        if self.size == self.capacity:
            self.resize()
        
        for i in range(self.size):
            if index == (self.size - (i + 1)):
                self.arr[self.size - (i + 1)] = value
                break
            else:
                self.arr[self.size - (i + 1)] = self.arr[self.size - (i + 2)]

    #Time complexity: O(1) - constant time
    def append(self, value):
        # TODO: remove 'pass' and implement functionality
        if (self.size >= self.capacity):
            self.resize()
        self.arr[self.size] = value
        self.size += 1

    #Time complexity: O(1) - constant time
    def set_at(self, value, index):
        # TODO: remove 'pass' and implement functionality
        if self.size <= index or index < 0:
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
        if (self.size <= index or index < 0):
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
        self.capacity *= 2
        index = 0
        temp = [0] * self.capacity
        for i in range(self.size):
            temp[index] = self.arr[i]
            index += 1
        self.arr = temp

    #Time complexity: O(n) - linear time in size of list
    def remove_at(self, index):
        # TODO: remove 'pass' and implement functionality
        if self.size <= index or index < 0 or self.size == 0:
            raise IndexOutOfBounds()
        for i in range(self.size + 1):
            if index == self.size:
                self.arr[self.size - 1] = 0
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
        new_arr = ArrayList()
        if start < 0 or start >= self.size or self.size <= (start + length):
            raise IndexOutOfBounds()
        for i in range(length):
            new_arr.append(self.arr[start + i])
        return new_arr

    #Time complexity: O(n) - linear time in size of concatinated list
    # OR
    #Time complexity: O(n+m) - linear time in size of both lists, self and other
    def concatenate(self, other):
        # TODO: remove 'pass' and implement functionality
        new_arr = ArrayList()
        for i in range(self.size):
            new_arr.append(self.arr[i])
        for i in range(other.size):
            new_arr.append(other.arr[i])
        return new_arr


if __name__ == "__main__":
    
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()
    arr_lis.append(4)
    arr_lis.append(12)
    arr_lis.append(8)
    arr_lis.append(3)
    # arr_lis.prepend(15)
    #arr_lis.insert(17, 4)
    # arr_lis.set_at(8, 0)
    # arr_lis.get_first()
    # arr_lis.get_at(4)
    # arr_lis.get_last()
    print(str(arr_lis))
    #arr_lis.remove_at(4)
    #print(str(arr_lis))