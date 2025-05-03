class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for curr in range(1, len(nums)):
            for prev in range(curr):
                if nums[curr] > nums[prev]:
                    dp[curr] = max(dp[prev]+1, dp[curr])
        return max(dp)
