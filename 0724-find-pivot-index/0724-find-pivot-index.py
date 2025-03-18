class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumleft = 0
        sumright = sum(nums)

        for i in range(len(nums)):
            sumright-=nums[i]
            if sumright == sumleft:
                return i
            sumleft+=nums[i]
        return -1

            