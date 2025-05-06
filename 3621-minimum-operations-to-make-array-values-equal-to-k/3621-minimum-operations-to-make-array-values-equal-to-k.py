class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
       
        distinct_max = set()
        for num in nums:
            if num < k:
                return -1
            if num != k:
                distinct_max.add(num)
        return len(distinct_max)