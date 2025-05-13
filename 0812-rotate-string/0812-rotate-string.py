class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        # target = goal[0]
        # for i in range(len(s)):
        #     if target == s[i]:
        #         new_str = s[i:] + s[:i]
        #         #print(new_str)
        #         if new_str == goal:
        #             return True
        # return False
        if len(s) != len(goal):
            return False
        lps = [0]*len(goal)
        prev =0
        i = 1

        while i < len(goal):
            if goal[i] == goal[prev]:
                prev+=1
                lps[i] = prev
                i+=1
            else:
                if prev != 0:
                    prev = lps[prev-1]
                else:
                    lps[i] = 0
                    i+=1
        

        i = 0
        j = 0
        s = s+s
        while i< len(s):
            if j == len(goal):
                return True
            
            if s[i] == goal[j]:
                i+=1
                j+=1
            else:
                if j !=0:
                    j = lps[j-1]
                else:
                    i+=1
        return False