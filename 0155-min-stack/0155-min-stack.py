class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minval:
            if val<= self.minval[-1]:
                self.minval.append(val)
        else:
            self.minval.append(val)

    def pop(self) -> None:
        pop = self.stack.pop()
        if pop == self.minval[-1]:
            self.minval.pop()
        return pop

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minval[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()