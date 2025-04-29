class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        # return 1162261467 % n ==0

        while n%3 == 0:
            n = n//3
        return n==1