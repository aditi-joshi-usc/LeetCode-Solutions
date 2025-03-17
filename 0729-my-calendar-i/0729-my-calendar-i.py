class MyCalendar:

    def __init__(self):
        self.track = defaultdict(int)

    def book(self, startTime: int, endTime: int) -> bool:
        
        self.track[startTime] +=1
        self.track[endTime] -=1          
        ans = True
        sumval=0
        for key in sorted(self.track):
            sumval += self.track[key]  
            if sumval > 1:
                ans = False
                break
        if not ans:
            self.track[startTime] -=1
            self.track[endTime] +=1  

        return ans


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)