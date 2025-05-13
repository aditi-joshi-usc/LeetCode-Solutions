class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        target = goal[0]
        for i in range(len(s)):
            if target == s[i]:
                new_str = s[i:] + s[:i]
                #print(new_str)
                if new_str == goal:
                    return True
        return False