class stack_implementation:
    def __init__(self, ptr=0, capacity=3):
        self.stack = [None]*capacity
        self.ptr=ptr
        self.capacity=capacity
    def isFull(self):
        return self.capacity==self.ptr

    def isEmpty(self):
        return self.ptr==0

    def expand(self):
        new_stack=[None]*(self.capacity*2)
        for i in range(self.capacity):
            new_stack[i] = self.stack[i]
        self.stack=new_stack
        self.capacity*=2
    def insert(self, val):
        if self.isFull():
            self.expand()
        self.stack[self.ptr]=val
        self.ptr+=1
    def pop(self):
        if self.isEmpty():
            return f"stack is already empty"
        self.ptr -= 1
        val=self.stack[self.ptr]
        self.stack[self.ptr]=None
        return val
    def __len__(self):
        return self.ptr



s = stack_implementation()
s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)  # triggers expansion
print(s.pop())  # 40
print(s.pop())  # 30
print(len(s))   # 2

