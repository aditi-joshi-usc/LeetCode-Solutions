class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0
        maxlen =0 
        len_nums = len(nums)
        zero_count =0 
        
        for r in range(len_nums):
            if nums[r] == 0:
                zero_count+=1
            
            if zero_count > k:
                if nums[l] == 0:
                    zero_count-=1
                l=l+1
            maxlen = max(maxlen, r-l+1)
        return maxlen
            