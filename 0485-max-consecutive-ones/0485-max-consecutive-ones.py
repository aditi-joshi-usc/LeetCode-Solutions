class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxsum = 0
        sum = 0
        for num in nums:
            if num == 0:
                maxsum = max(maxsum, sum)
                sum=0
            else:
                sum+=1
        maxsum = max(maxsum, sum)
        return maxsum