class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        maxsum = float('-inf')

        sumval = 0

        for i in range(len(nums)):
            sumval+= nums[i]

            maxsum = max(maxsum, sumval)

            if sumval<0:
                sumval = 0
        return maxsum

