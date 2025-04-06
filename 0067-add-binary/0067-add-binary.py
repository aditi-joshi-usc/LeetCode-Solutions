class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0

        a = list(a)
        b = list(b)

        res =[]
        while a or b:
            sumval = 0
            if a:
                sumval += int(a.pop())
            if b:
                sumval += int(b.pop())
            sumval+=carry
            res.append(str(sumval%2))
            carry = sumval//2
        if carry:
            res.append('1')  
        
        return ''.join(res[::-1])


            
        
        