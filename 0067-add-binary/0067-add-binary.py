class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        i = len(a)-1
        j = len(b)-1
        res =[]
        while i>=0 or j>=0:
            sumval = 0
            if i>=0:
                sumval += int(a[i])
                i-=1
            if j>=0:
                sumval += int(b[j])
                j-=1
            sumval+=carry
            res.append(str(sumval%2))
            carry = sumval//2
        if carry:
            res.append('1')  
        
        return ''.join(res[::-1])


            
        
        