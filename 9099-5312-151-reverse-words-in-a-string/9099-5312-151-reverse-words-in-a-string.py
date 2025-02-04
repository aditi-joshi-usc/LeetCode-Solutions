class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        # s = s.strip().split()
        # ans = ""
        # for i in range(len(s)-1, -1, -1):
        #     if s[i] != " ":
        #         ans += s[i] 
        #     if i!=0:
        #         ans+=" "
        
        # return ans
        s = s.strip()
        while "  " in s:
            s = s.replace("  ", " ")
        s = s.split()
        s = s[::-1]

        return ' '.join(s)
