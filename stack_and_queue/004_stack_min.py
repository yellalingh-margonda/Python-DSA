class stack_implement:

    def __init__(self, capacity=3, ptr=0):
        self.capacity = capacity
        self.ptr = ptr
        self.stack = [None] * self.capacity

    def isFull(self):
        return self.ptr == self.capacity

    def isEmpty(self):
        return self.ptr == 0

    def expand(self):
        new_stack = [None] * (self.capacity * 2)
        for i in range(self.ptr):
            new_stack[i] = self.stack[i]
        self.stack = new_stack
        self.capacity *= 2

    def insert(self, val):
        if self.isFull():
            self.expand()
        current_min = val if self.isEmpty() else min(val, self.stack[self.ptr - 1][1])
        self.stack[self.ptr] = (val, current_min)
        self.ptr += 1

    def getMini(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack[self.ptr - 1][1]

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        self.ptr -= 1
        val = self.stack[self.ptr][0]
        self.stack[self.ptr] = None
        return val
s = stack_implement()
s.insert(5)
s.insert(3)
s.insert(7)
s.insert(2)
print(s.getMini())  # 2
s.pop()
print(s.getMini())  # 3
s.pop()
print(s.getMini())  # 3
s.pop()
print(s.getMini())  # 5
