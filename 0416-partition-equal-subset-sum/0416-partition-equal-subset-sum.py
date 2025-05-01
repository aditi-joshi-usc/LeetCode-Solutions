class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        sumnum = sum(nums)
        if sumnum%2 != 0:
            return False
        halfsum = sumnum/2
        track ={}
        def backtrack(index, curr_sum):
            if curr_sum == halfsum:
                return True
            if index >= len(nums) or curr_sum >halfsum:
                return False
            if (index, curr_sum) in track:
                return track[(index, curr_sum)]
            
            track[(index, curr_sum)] = backtrack(index+1, curr_sum+nums[index]) or backtrack(index+1, curr_sum)
            return track[(index, curr_sum)]


    
        return backtrack(0, 0)
