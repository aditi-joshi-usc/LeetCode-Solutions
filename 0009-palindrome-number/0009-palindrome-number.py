class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal = []
        num = x
        if num<0:
            return False
        while num:
            pal.append(num%10)
            num = num//10
        
        return pal == pal[::-1]