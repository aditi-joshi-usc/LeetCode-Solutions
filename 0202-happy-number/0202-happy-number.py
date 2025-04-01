class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        def happynum(n):
            if n in visited:
                return False
            sumval = 0
            visited.add(n)
            while n>0:
                sumval+=(n%10)**2
                n=n//10
            if sumval == 1:
                return True
            else:
                
                return happynum(sumval)
      
        return happynum(n)