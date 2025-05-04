class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1] * len(nums)

        # for curr in range(1, len(nums)):
        #     for prev in range(curr):
        #         if nums[curr] > nums[prev]:
        #             dp[curr] = max(dp[prev]+1, dp[curr])
        # return max(dp)
        #sub = []

        # for num in nums:
        #     i = bisect_left(sub, num)

        #     if i == len(sub):
        #         sub.append(num)
        #     else: 
        #         sub[i] = num
        # return len(sub)

        sub = []


        for num in nums:

            left = 0
            right = len(sub)

            while left < right:
                mid = (left+right)//2

                if sub[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            
            if left == len(sub):
                sub.append(num)
            else:
                sub[left] = num
        return len(sub)
