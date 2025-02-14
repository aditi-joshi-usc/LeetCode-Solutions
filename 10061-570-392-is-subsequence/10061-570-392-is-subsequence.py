class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # for ssub in s:
        #     if ssub in t:
        #         for tt in t:
        #             if tt == ssub:
        #                 break
        #             else:
        #                 t = t[1:]
        #         t = t[1:]
        #     else:
        #         return False
        # return True
        

        count = 0

        for char in t:
            if count< len(s) and s[count] == char:
                count+=1
        return count == len(s)