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
        if self.arr != []:
            for i in range(self.size):
                return_string += (str(self.arr[i]) + ", ")
        return return_string[:-2]

    #Time complexity: O(n) - linear time in size of list
    def prepend(self, value):
        # TODO: remove 'pass' and implement functionality
        if self.size == self.capacity:
            self.resize()
        self.size += 1
        for i in range(self.size):
            self.arr[self.size - (i + 1)] = self.arr[self.size - (i + 2)]
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
        position = self.size
        while position > index:
            self.arr[position] = self.arr[position - 1]
            position -= 1
        self.arr[index] = value



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
        if self.size <= index or self.size == 0 or self.size < 0 or index < 0:
            raise IndexOutOfBounds()
        self.arr[index] = value

    #Time complexity: O(1) - constant time
    def get_first(self):
        # TODO: remove 'pass' and implement functionality
        if self.size == 0 or self.size < 0:
            raise Empty()
        return self.arr[0]

    #Time complexity: O(1) - constant time
    def get_at(self, index):
        # TODO: remove 'pass' and implement functionality
        if self.size <= index or self.size < 0 or index < 0:
            raise IndexOutOfBounds()
        return self.arr[index]

    #Time complexity: O(1) - constant time
    def get_last(self):
        # TODO: remove 'pass' and implement functionality
        if self.size == 0 or self.size < 0:
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

        if self.size <= index or self.size == 0 or self.size < 0 or index < 0:
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
        new_list = ArrayList()
        #index = 0
        #return_string = ""
        #new_list = [0] * length
        if start >= self.size or start < 0 or (start + length) >= self.size:
            raise IndexOutOfBounds()
        for i in range(length):
            if self.arr[start+i] == 0:
                raise IndexOutOfBounds()
            if self.arr[start+i] != 0:
                new_list.append(self.arr[start+i])
                #new_list[index] = self.arr[start+i]
            #index += 1
        #for i in range(length):
            #return_string += (str(new_list[i]) + ", ")
        #return return_string[:-2]
        return new_list



    #Time complexity: O(n) - linear time in size of concatinated list
    # OR
    #Time complexity: O(n+m) - linear time in size of both lists, self and other
    def concatenate(self, other):
        # TODO: remove 'pass' and implement functionality
        new_list = ArrayList()
        #index = 0
        #return_string = ""
        self.capacity = self.size + other.size
        #new_list = [0] * self.capacity
        for i in range(self.size):
            new_list.append(self.arr[i])
            #new_list[index] = self.arr[i]
            #index += 1
        for i in range(other.size):
            new_list.append(other.arr[i])
            #new_list[index] = self.arr[i]
            #index += 1
        #self.arr = new_list
        #for i in range((self.size+other.size)):
        #    return_string += (str(new_list[i]) + ", ")
        #return return_string[:-2]
        return new_list


if __name__ == "__main__":
    pass
    # add your tests here or in a different file.
    # Do not add them outside this if statement
    # and make sure they are at this indent level

    arr_lis = ArrayList()

    print(str(arr_lis))
