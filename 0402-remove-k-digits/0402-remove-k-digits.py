class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 1432219

        # stack = []
        # 1 => stack = [1,]
        # 4 => stack = [1,4]
        # 3 => stack = [1,3]
        # 2 => stack = [1,2,2]
        # 2 => stack = [1,2,2]
        # 1 => stack = [1,2,1]
        # 9 => stack = [1,2,1,9]
        
        stack = []

        for char in num:

            while stack and k>0 and stack[-1] > char:
                stack.pop()
                k-=1
            stack.append(char)

        stack = stack[: len(stack) - k]
        return ''.join(stack).lstrip('0') or '0'
        
