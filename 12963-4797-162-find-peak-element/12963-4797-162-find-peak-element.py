class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        #Time complexity = O(n)
        # peak = 0

        # for i in range(1,len(nums)):
        #     if nums[i] > nums[i-1] :
        #         if i+1< len(nums):
        #             if nums[i] > nums[i+1]:
        #                 if nums[peak] < nums[i]:
        #                     peak = i
        #         else:
        #             if nums[peak] < nums[i]:
        #                     peak = i
        

        # return peak

        #Pointer Time complexity = O(n)
        # if len(nums) == 1:
        #     return 0
        
        # l = 0
        # r = l

        # peak = -1
        # peak_val = float('-inf')
        # while r< len(nums):
        #     if nums[r] > peak_val:
        #         peak_val = nums[r]
        #         peak = r
        #         r+=1
        #     else:
        #         return peak
        # return peak


        if len(nums) == 1:
            return 0
        n = len(nums)
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1

        start = 1
        end = n-1

        while start <= end:
            mid = start + (end - start)//2
            
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid-1]:
                end = mid - 1
            elif nums[mid] < nums[mid+1]:
                start = mid + 1
        return -1
            