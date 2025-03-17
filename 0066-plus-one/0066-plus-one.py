class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1

        for i in range(len(digits) -1, -1, -1):
            sumval = 0
            sumval = digits[i] + carry
            
            digits[i] = sumval % 10
            carry = sumval //10
        if carry:
            digits = [carry] + digits
        return digits 
            