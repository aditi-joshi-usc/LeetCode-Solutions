class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        k = len(nums)

        position = 1
        repeat = 0
        while position < k:
            if nums[position]  == nums[position - 1]:
                if repeat >= 1:
                    nums.pop(position)
                    k-=1
                else: 
                    repeat+=1
                    position+=1
            else:
                repeat = 0
                position+=1
        return k



