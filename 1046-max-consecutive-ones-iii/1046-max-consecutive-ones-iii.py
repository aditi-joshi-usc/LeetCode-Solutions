class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        l = 0
        maxlen =0 
        len_nums = len(nums)
        running_count =0 
        
        for r in range(len_nums):
            k-=1-nums[r]

            if k<0:
                k+= 1-nums[l]
                l+=1
        return r - l +1

            