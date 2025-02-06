class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        ans =''
        for char in s:
            if char.isalnum():
                ans+=char
        
        return ans == ans[::-1]

        