class Solution:
    def countPrimes(self, n: int) -> int:
        
        nums = [False, False] + [True]*(n-2)

        for p in range(2, int(sqrt(n))+1):
            if nums[p]:

                for multiples in range(p*p,n, p):
                    nums[multiples] = False
        return sum(nums)