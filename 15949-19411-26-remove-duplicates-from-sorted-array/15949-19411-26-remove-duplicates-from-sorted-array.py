class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        position =1
        k = len(nums)
        while position < k:
            if nums[position] == nums[position - 1]:
                nums.pop(position)
                k-=1
            else:
                position+=1
        return k
        


        