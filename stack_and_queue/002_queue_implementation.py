class queue_implementation:
    def __init__(self, size=0, capacity=3):
        self.queue = [None] * capacity
        self.size = size
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def expand(self):
        new_queue = [None] * (self.capacity * 2)
        for i in range(self.capacity):
            new_queue[i] = self.queue[i]
        self.queue = new_queue
        self.capacity *= 2

    def insert(self, val):
        if self.isFull():
            self.expand()
        self.queue[self.size] = val
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Queue is already empty"
        val = self.queue[0]
        for i in range(1, self.size):
            self.queue[i - 1] = self.queue[i]
        self.queue[self.size - 1] = None
        self.size -= 1
        return val

    def __len__(self):
        return self.size
