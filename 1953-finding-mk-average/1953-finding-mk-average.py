class MKAverage:

    def __init__(self, m: int, k: int):
        self.q = deque()
        self.m = m
        self.k = k

        self.low = SortedList()
        self.mid = SortedList()
        self.high = SortedList()
        self.curr_sum = 0



    def addElement(self, num: int) -> None:

        if not self.low or self.low[-1] >= num:
            self.low.add(num)
        elif not self.high or self.high[0]<= num:
            self.high.add(num)
        else:
            self.mid.add(num)
            self.curr_sum+=num
        self.q.append(num)

        while len(self.q) > self.m:
            oldest_element = self.q.popleft()
            if oldest_element in self.low:
                self.low.remove(oldest_element)
            elif oldest_element in self.high:
                self.high.remove(oldest_element)
            else:
                self.mid.remove(oldest_element)
                self.curr_sum-=oldest_element



        self.rebalance_lists()
    
    def rebalance_lists(self):

        while len(self.low)>self.k:
            biggest_element = self.low.pop()
            self.mid.add(biggest_element)
            self.curr_sum+= biggest_element
        while len(self.high)>self.k:
            smallest_element = self.high.pop(0)
            self.mid.add(smallest_element)
            self.curr_sum+= smallest_element
        while len(self.low)<self.k and self.mid:
            smallest_element = self.mid.pop(0)
            self.low.add(smallest_element)
            self.curr_sum-= smallest_element
        while len(self.high)<self.k and self.mid:
            biggest_element = self.mid.pop()
            self.high.add(biggest_element)
            self.curr_sum-= biggest_element
        

        
    


        

    def calculateMKAverage(self) -> int:
        if len(self.q) < self.m:
            return -1
        
        return self.curr_sum // (self.m - 2*self.k)
        


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()