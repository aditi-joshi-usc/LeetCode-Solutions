class RandomizedSet:

    def __init__(self):
        self.obj = set()
        return None
        

    def insert(self, val: int) -> bool:
        if val in self.obj:
            return False
        else:
            self.obj.add(val)
            return True 

    def remove(self, val: int) -> bool:
        if val in self.obj:
            self.obj.remove(val)
            return True
        else:
            return False 
 

    def getRandom(self) -> int:
        return random.choice(list(self.obj))
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()