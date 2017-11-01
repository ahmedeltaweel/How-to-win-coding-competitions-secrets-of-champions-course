from edx_io import edx_io
from collections import deque


class Node(object):
    '''
    Singly-linked list node for storing data in
    a queue
    '''

    def __init__(self, data=None):
        '''
        Initialise a Node with optional data to be stored
        '''
        self.right = None
        self.data = data
        self.prevMin = None


class Queue(object):
    '''
    Queue structure implemented using a singly-linked list
    '''

    def __init__(self):
        '''
        Initialise an empty queue
        '''
        self.first = None
        self.last = None
        self._min = None

    def enqueue(self, data):
        '''
        Enqueue data; putting it on the back of the queue
        '''
        new_node = Node(data)
        if self.first is None and self.last is None:
            # case 1: no nodes exist
            self.first = new_node
            self.last = self.first
            self._min = data
        else:
            # case 2: at least one node exists
            if data < self._min:
                new_node.prevMin = self._min
                self._min = data

            self.last.right = new_node
            self.last = new_node

    def dequeue(self):
        '''
        Dequeue data; removing it from the front of the queue
        '''
        if self.first is None:
            # case 1: nothing on the queue
            return None
        else:
            # case 2: something on the queue
            data = self.first.data
            next = self.first.right
            if next is None:
                # case 1: nothing else queued
                self.first = None
                self.last = None
                self._min = None
            else:
                # case 2: something else queued
                if data == self._min:
                    if self.first.prevMin is None:
                        walker = self.
                    else:
                        self._min = self.first.prevMin
                self.first = next

            return data

    def get_min(self):
        return self._min


if __name__ == '__main__':
    l = Queue()
    with edx_io() as io:
        n = int(io.next_int())
        for i in range(n):
            ops = io.next_token().decode('utf-8')
            if ops == '+':
                inp = int(io.next_token().decode('utf-8'))
                l.enqueue(inp)
            elif ops == '-':
                l.dequeue()
            elif ops == '?':
                io.writeln(l.get_min())
