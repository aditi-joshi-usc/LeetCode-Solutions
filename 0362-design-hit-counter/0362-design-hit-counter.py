class HitCounter:

    def __init__(self):
        self.tstamp = []

    def hit(self, timestamp: int) -> None:
        self.tstamp.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        
        time_valid = timestamp-300
        count = 0
        for time in self.tstamp:
            if time > time_valid:
                count+=1
        return count



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)