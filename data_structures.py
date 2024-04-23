# Author(s): David Tang

class Stack:

    def __init__(self, cap=10):
        self.cur_size = 0
        self.stack = [None] * cap

    def capacity(self):
        return len(self.stack)

    def push(self, data):
        # Max out case
        if len(self.stack) == self.cur_size:
            new_stack = [None] * len(self.stack) * 2
            # Transfer data from old stack to new stack
            for i in range(self.cur_size):
                new_stack[i] = self.stack[i]
            del self.stack
            # Add data at the back of array
            new_stack[self.cur_size] = data
            self.cur_size += 1
            self.stack = new_stack
        else: # Under capacity case
            self.stack[self.cur_size] = data
            self.cur_size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError('pop() used on empty stack')
        else:
            # To delete a element in stack, set it to 'None'
            top = self.stack[self.cur_size - 1]
            self.stack[self.cur_size - 1] = None
            self.cur_size -= 1
            return top

    def get_top(self):
        if self.is_empty():
            return None
        else:
            return self.stack[self.cur_size - 1]

    def is_empty(self):
        return self.cur_size == 0

    def __len__(self):
        return self.cur_size


class Queue:
    # Treat our queue as rounded array, the front_index is
    # the start of array and the back_index is the end array.
    def __init__(self, cap=10):
        self.cur_size = 0
        self.queue = [None] * cap
        self.front_index = 0
        self.back_index = 0

    def capacity(self):
        return len(self.queue)

    # This function will enqueue new data into the right side back_index.
    def enqueue(self, data):
        if len(self.queue) == self.cur_size:
            new_queue = [None] * len(self.queue) * 2
            # Transfer data to new queue
            for i in range(self.cur_size):
                # Starting 0 index of new queue
                new_queue[i] = self.queue[self.front_index]
                # Move front_index 1 position to the right in every loop
                self.front_index = (self.front_index + 1) % len(self.queue)
            # Insert data to back of new queue
            new_queue[self.cur_size] = data
            # Reset front and back index pointer
            self.front_index = 0
            self.back_index = self.cur_size
            self.cur_size += 1
            del self.queue
            self.queue = new_queue
        else:
            # When queue is empty it do not move back_index
            # Else Move back_index 1 position to the right
            if self.is_empty() is False:
                self.back_index = (self.back_index + 1) % len(self.queue)
            self.queue[self.back_index] = data
            self.cur_size += 1

    # This function will remove element in front_index then move
    # it's position 1 to the right. Function return removed element
    def dequeue(self):
        if self.is_empty():
            raise IndexError('dequeue() used on empty queue')
        else:
            # Get a copy of front element
            front = self.queue[self.front_index]
            # Set front element to 'None'
            self.queue[self.front_index] = None
            # If the front and back not pointing the same element,
            # it move front_index 1 position to the right.
            if self.cur_size != 1:
                self.front_index = (self.front_index + 1) % len(self.queue)
            self.cur_size -= 1
            return front

    def get_front(self):
        if self.is_empty():
            return None
        else:
            return self.queue[self.front_index]

    def is_empty(self):
        return self.cur_size == 0

    def __len__(self):
        return self.cur_size


class Deque:
    # Same as queue, treat array as linked on start and end.
    def __init__(self, cap=10):
        self.cur_size = 0
        self.deque = [None] * cap
        self.front_index = 0
        self.back_index = 0

    def capacity(self):
        return len(self.deque)

    # Push a element on left side of current front_index position
    def push_front(self, data):
        if len(self.deque) == self.cur_size:
            # If over capacity, create new deque
            # and put new data into first index.
            new_deque = [None] * len(self.deque) * 2
            new_deque[0] = data
            # Start from the second index of new deque,
            # transfer data from old deque to new deque.
            for i in range(1, self.cur_size+1):
                new_deque[i] = self.deque[self.front_index]
                self.front_index = (self.front_index + 1) % len(self.deque)
            # Reset front and back index pointer
            self.front_index = 0
            self.back_index = self.cur_size
            self.cur_size += 1
            del self.deque
            self.deque = new_deque
        else:
            # When no element in array it do not move index pointer,
            # else it move front_index pointer 1 position to left.
            if self.is_empty() is False:
                self.front_index = (self.front_index - 1) % len(self.deque)
            self.deque[self.front_index] = data
            self.cur_size += 1

    # Push a element on right side of current back_index position
    def push_back(self, data):
        if len(self.deque) == self.cur_size:
            new_deque = [None] * len(self.deque) * 2
            # Start from first index of new deque,
            # transfer data from old deque to new deque
            for i in range(len(self.deque)):
                new_deque[i] = self.deque[self.front_index]
                self.front_index = (self.front_index + 1) % len(self.deque)
            # Place insert data at end of new deque
            # Reset front and back index pointer
            new_deque[self.cur_size] = data
            self.front_index = 0
            self.back_index = self.cur_size
            self.cur_size += 1
            del self.deque
            self.deque = new_deque
        else:
            # When no element in array it do not move index pointer,
            # else it move back_index pointer 1 position to right.
            if self.is_empty() is False:
                self.back_index = (self.back_index + 1) % len(self.deque)
            self.deque[self.back_index] = data
            self.cur_size += 1

    def pop_front(self):
        if self.is_empty():
            raise IndexError('pop_front() used on empty deque')
        else:
            front = self.deque[self.front_index]
            self.deque[self.front_index] = None
            # If there is only one element left, it do not need to
            # move pointer after remove. Else move front_index pointer
            # 1 position to the right of array.
            if self.cur_size != 1:
                self.front_index = (self.front_index + 1) % len(self.deque)
            self.cur_size -= 1
            return front

    def pop_back(self):
        if self.is_empty():
            raise IndexError('pop_back() used on empty deque')
        else:
            back = self.deque[self.back_index]
            self.deque[self.back_index] = None
            # If there is only one element left, it do not need to
            # move pointer after remove. Else move back_index pointer
            # 1 position to the left of array.
            if self.cur_size != 1:
                self.back_index = (self.back_index - 1) % len(self.deque)
            self.cur_size -= 1
            return back

    def get_front(self):
        if self.is_empty():
            return None
        else:
            return self.deque[self.front_index]

    def get_back(self):
        if self.is_empty():
            return None
        else:
            return self.deque[self.back_index]

    def is_empty(self):
        return self.cur_size == 0

    def __len__(self):
        return self.cur_size

    # Return a item in index 'k', raise a error if out of range
    def __getitem__(self, k):
        if abs(k) < len(self.deque):
            # 'k' work with negative index as long as 'k' within index range.
            return self.deque[(self.front_index + k) % len(self.deque)]
        else:
            raise IndexError('Index out of range')
