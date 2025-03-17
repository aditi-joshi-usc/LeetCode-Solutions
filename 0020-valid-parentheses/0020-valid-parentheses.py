class Solution:
    def isValid(self, s: str) -> bool:
        track = {
            ')' : '(',
            '}' : '{',
            ']' : '[' 
        }

        stack = []

        for char in s:
            if stack and char in track and stack[-1] == track[char]:
                stack.pop()
            else:
                stack.append(char)
        
        if len(stack) == 0:
            return True
        else:
            return False
        