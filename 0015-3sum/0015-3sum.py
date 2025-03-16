class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        j = 0 
        k = len(nums) -1 
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            j = i+1 
            k = len(nums) -1 
            while j<k and j< len(nums) and k< len(nums):
                sumval = nums[i] + nums[j] + nums[k]
                if  sumval == 0 :
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    while j < k and nums[j] == nums[j-1]:
                        j+=1
                elif sumval < 0 :
                    j+=1
                else:
                    k-=1
        return res
            
                    
            