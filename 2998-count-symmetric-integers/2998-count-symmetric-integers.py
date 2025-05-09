class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        

        count = 0
        
        for i in range(low, high+1):
            num = str(i)
            if len(num) % 2 != 0:
                continue
            n = len(num)//2
            
            n1 = [int(x) for x in num[:n]]
            n1 = sum(n1)
            n2 = [int(x) for x in num[n:]]
            n2 = sum(n2)
            if n1 == n2:
                count+=1
        return count

