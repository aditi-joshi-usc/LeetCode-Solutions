class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        

        low = 0
        
        if not nums:
            return []
        
        res = []
        for high in range(1, len(nums)):
            if nums[high] - nums[high -1] == 1 or high == low:
                continue
            else:
                if low == high-1:
                    res.append(str(nums[low]))
                else:
                    res.append(str(nums[low])+'->'+str(nums[high-1]))
                low = high 
        if low == len(nums)-1:
            res.append(str(nums[low]))
        elif low<len(nums):
            res.append(str(nums[low])+'->'+str(nums[-1]))
        
        return res


