class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        

        left = 0
        right = len(nums) -1
        res = [0]*len(nums)
        ind = len(nums)-1
        while left <= right:

            lsquare = nums[left]**2
            rsquare = nums[right]**2

            if lsquare > rsquare:
                res[ind] = lsquare
                left+=1
            
            else:
                res[ind] = rsquare
                right-=1
            ind-=1
        return res
