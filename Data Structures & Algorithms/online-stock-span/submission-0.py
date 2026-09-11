class StockSpanner:

    def __init__(self):
        self.seq = []
        

    def next(self, price: int) -> int:

        dummy = self.seq.copy()
        span = 1

        while dummy:
            curr = dummy.pop()

            if curr <= price:
                span += 1
            else:
                break
        
        self.seq.append(price)

        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)