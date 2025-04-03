class Solution:
    def calculate(self, s: str) -> int:
        stack, sign =[], 1

        ans =0 
        num =0
        for c in s:
            if c.isdigit():
                num = 10*num + int(c)
            elif c in '+-':
                ans += sign * num

                if c == '-':
                    sign = -1
                else:
                    sign = 1
                num = 0
            elif c =='(':
                stack.append(ans)
                stack.append(sign)
                ans = 0
                sign = 1
            elif c == ')':
                ans += sign*num
                num = 0
                
                prev_sign = stack.pop()
                prev_ans = stack.pop()
                
                ans = prev_ans+  prev_sign * ans
                
                sign=1
        return ans + (sign*num)


        
        
