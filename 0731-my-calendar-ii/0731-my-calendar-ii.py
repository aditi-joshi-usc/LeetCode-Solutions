class MyCalendarTwo:

    # def __init__(self):
    #     self.track = defaultdict(int)
        

    # def book(self, startTime: int, endTime: int) -> bool:
    #     self.track[startTime] +=1
    #     self.track[endTime] -=1

    #     ans = True
    #     sumval = 0
    #     for key in sorted(self.track):
    #         sumval+= self.track[key]
    #         if sumval>2:
    #             ans = False
    #             break
    #     if not ans:
    #         self.track[startTime] -=1
    #         self.track[endTime] +=1
    #     return ans




    def __init__(self):
        
        self.single_bookings = []
        self.double_bookings = []


    def book(self, startTime: int, endTime: int) -> bool:
        
        for dstart, dend in self.double_bookings:

            if max(dstart, startTime) < min(dend, endTime):
                return False
        

        for sstart, send in self.single_bookings:

            if max(sstart, startTime) < min(send, endTime):
                self.double_bookings.append([max(sstart, startTime), min(send, endTime)])
        
        self.single_bookings.append([startTime, endTime])
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)