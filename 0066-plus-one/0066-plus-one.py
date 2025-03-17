class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # carry = 1

        # for i in range(len(digits) -1, -1, -1):
        #     sumval = 0
        #     sumval = digits[i] + carry
            
        #     digits[i] = sumval % 10
        #     carry = sumval //10
        # if carry:
        #     digits = [carry] + digits
        # return digits 

        for i in range(len(digits) -1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + digits 

            