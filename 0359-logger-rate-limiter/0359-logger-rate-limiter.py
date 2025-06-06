class Logger:

    def __init__(self):
        self.track = {}


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        
        if message in self.track:
            if timestamp-self.track[message] >= 10:
                self.track[message]=timestamp
                return True
            else:
                return False
        else:
            self.track[message]=timestamp
            return True
        



# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)