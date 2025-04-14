class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal = 0
        num = x
        if num<0 or (num%10 == 0 and num!=0):
            return False
        while num:
            pal = pal *10 + (num%10)
            num = num//10
        
        return pal == x