class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        if len(s) == 0:
            return s
        
        stack = []

        for char in s:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        
        return ''.join(stack)
