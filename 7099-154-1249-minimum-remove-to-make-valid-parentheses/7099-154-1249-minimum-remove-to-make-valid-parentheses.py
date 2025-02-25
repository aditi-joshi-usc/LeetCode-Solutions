class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # open1 = 0
        # closed = 0
        # res = ''
        # flag =0
        # for i in range(len(s)):
        #     if s[i] == '(':
        #         open1+=1
        #         flag += 1
        #     elif s[i] == ')' and flag>0:
        #         closed+=1
        #         flag-=1   
        
        # open1 = min(open1,closed)  
        # closed = open1
        
        # for i in range(len(s)):
        #     if s[i] =='(':
        #         if open1 > 0:
        #             res+=s[i]
        #             open1-=1
        #         continue
        #     if s[i] == ')':
        #         if closed > 0 and closed > open1:
        #             res+=s[i]
        #             closed-=1
        #         continue    
        #     else:
        #         res+=s[i]
                
        # return res

        s = list(s)
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            if s[i] ==')':
                if stack:
                    stack.pop()
                else:
                    s[i]=''                     
        
        for i in stack:
            s[i]=''
        return ''.join(s)