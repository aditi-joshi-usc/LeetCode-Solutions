class Solution:

    def power_func(self,x,n):
        if n == 0:
            return 1
        if n%2 == 0:
            half_val = self.power_func(x, n/2)
            return half_val*half_val
        return self.power_func(x, n-1)*x

    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x = 1/x
            n =-n
        return self.power_func(x,n)
        