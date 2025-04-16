class Solution:
    def sum(self, num1: int, num2: int) -> int:
        left = -200
        right = 200

        while left<right:
            mid = (left + right)//2
            if mid == num1+num2:
                return mid
            elif mid> num1+num2:
                right = mid-1
            else:
                left = mid + 1
        return left
