class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff_arr = [0] *(len(nums)+1)

        for start, end in queries:
            diff_arr[start] +=1
            if end + 1 < len(nums): 
                diff_arr[end+1] -=1
        
        prefix = 0
        for i in range(len(nums)):
            prefix += diff_arr[i]
            if nums[i]> prefix :
                return False
        return True
