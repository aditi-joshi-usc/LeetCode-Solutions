class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        l = len(nums)
        i=0
        while i < l:
            if nums[i] == val:
                
                nums.pop(i)

                nums.append('_')
            else:
                #cnt+=1
                i+=1

        for i in nums:
            if i == "_":
                nums.remove(i)
            else:
                cnt+=1
        return cnt


        