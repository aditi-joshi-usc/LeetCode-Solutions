class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        num1, num2 = num1[::-1], num2[::-1]

        l1 = len(num1)
        l2 = len(num2)
        l3 = max(l1, l2)
        i=0
        carry = 0
        res=[]
        while i < l3 or carry:
            
            dig1 = (ord(num1[i]) - ord('0')) if i < l1 else 0
            dig2 = (ord(num2[i]) - ord('0')) if i < l2 else 0

            sumval = dig1 + dig2 + carry
            carry = sumval // 10
            sumval = sumval % 10
            res.append(str(sumval))
            i+=1
        
        return ''.join(res[::-1])
