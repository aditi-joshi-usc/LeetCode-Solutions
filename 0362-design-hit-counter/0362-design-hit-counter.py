class HitCounter:

    def __init__(self):
        self.tstamp = deque()

    def hit(self, timestamp: int) -> None:
        self.tstamp.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        
        while self.tstamp and timestamp - self.tstamp[0] >=300:
            self.tstamp.popleft()
        return len(self.tstamp)




# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)