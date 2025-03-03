class MovingAverage:

    def __init__(self, size: int):
        self.q= deque()
        self.size = size
        self.window_sum = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            removed = self.q.popleft()
            self.window_sum -= removed
        self.q.append(val)
        self.window_sum += val
        return self.window_sum/len(self.q)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)