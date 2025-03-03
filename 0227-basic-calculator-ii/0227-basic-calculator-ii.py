class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        temp = 0
        last_sign = '+'
        num=0
        for i in range(len(s)):
            if s[i].isnumeric():
                num = 10*num+ int(s[i])
            
            if i == len(s) -1 or s[i].isnumeric() == False and s[i] != ' ':
                if last_sign =='+':
                    res+=temp
                    temp = num
                elif last_sign =='-':
                    res+=temp
                    temp = -num
                elif last_sign == '*':
                    temp *= num
                elif last_sign =='/':
                    temp = int(temp/num)
                last_sign = s[i]
                num = 0
        
        res+=temp
        return res
