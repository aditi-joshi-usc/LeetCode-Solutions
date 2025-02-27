class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        hmap = {0:1}

        for num in nums:
            
            prefix_sum += num

            if prefix_sum - k in hmap:
                count += hmap[prefix_sum - k]
            if prefix_sum in hmap:
                hmap[prefix_sum] +=1
            else:
                hmap[prefix_sum] =1
        return count