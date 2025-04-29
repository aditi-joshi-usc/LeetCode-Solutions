class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxnum = len(nums)+1
        for i in range(maxnum):
            if i not in nums:
                return i
        return -1