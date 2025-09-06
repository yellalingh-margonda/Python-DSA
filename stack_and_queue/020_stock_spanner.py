class StockSpanner:

    def __init__(self):
        self.capacity=5
        self.prices=[None]*self.capacity
        self.ptr=0
    def isfull(self):
         return self.ptr==self.capacity
    def extend(self):
        new_prices=[None]*self.capacity*2
        for i in range(self.ptr):
            new_prices[i]=self.prices[i]
        self.capacity=2*self.capacity
        self.prices=new_prices
    def next(self, price: int) -> int:
        if self.isfull():
            self.extend()
        self.prices[self.ptr]=price
        self.ptr+=1
        span=1
        for i in range(self.ptr-2,-1,-1):
            if self.prices[i]<=price:
                span+=1
            else:
                break
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)