class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minval= min(nums)
        if minval < k:
            return -1
        distinct_max = set()
        for num in nums:
            if num != k:
                distinct_max.add(num)
        return len(distinct_max)