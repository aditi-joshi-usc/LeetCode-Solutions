class Solution:
    def myPow(self, x: float, n: int) -> float:


        def findpow(x,n):
            if n<=0:
                return 1
            if n == 1:
                return x
            if n ==2:
                return x*x
            half=findpow(x,n//2)
            if n%2 == 0:
                return half * half
            else:
                return x* half * half


        if x == 0:
            return 0
        if n<0:
            x = 1/x
            n = -n
        
        return findpow(x,n)
        