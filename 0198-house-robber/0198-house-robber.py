class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0]*(len(nums) + 1)
        dp[1] = nums[0]

        for i in range(1, len(nums)):
            dp[i+1] = max(nums[i]+dp[i-1], dp[i])
        return dp[len(nums)]