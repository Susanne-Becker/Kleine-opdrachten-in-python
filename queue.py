# Implements a queue
class Queue:
    def __init__(self):
        self._data = []

    # add element to back of queue
    def enqueue(self, element):
        self._data.append(element)

    def peek(self): #3
        return self._data[0]

    def size(self): #2
        return len(self._data)

    # remove and return element from front of queue
    def dequeue(self):
        assert self.size() > 0
        return self._data.pop(0)

    def empty(self): #0
        return self._data.clear()

q = Queue()          # create new queue
q.enqueue(3)         # add number 3 to back of queue
q.enqueue(1)         # add number 1 to back of queue
print(q.peek())      # 3
print(q.size())      # 2
print(q.dequeue())   # prints first number "in", so 3
print(q.empty())     # 0