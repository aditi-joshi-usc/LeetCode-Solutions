class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_chars = []
        target_chars=[]
      
        for i, s in enumerate(start):
            if s != '_':
                start_chars.append((s,i))
            
        
        for i, s in enumerate(target):
            if s != '_':
                target_chars.append((s,i))
        
        if len(start_chars) != len(target_chars):
            return False
        
        for i in range(len(start_chars)):
            if start_chars[i][0] != target_chars[i][0]:
                return False
            if start_chars[i][0] =='L' and start_chars[i][1] < target_chars[i][1]:
                return False
            if start_chars[i][0] =='R' and start_chars[i][1] > target_chars[i][1]:
                return False
            
        return True
