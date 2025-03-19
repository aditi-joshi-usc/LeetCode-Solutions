class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        

        left = 0
        right = len(arr) -1
        nums =arr
        # while left != right:
        #     mid = left + (right- left) //2
            
        #     if nums[mid] >= nums[mid+1]:
        #         right = mid
        #     else:
        #         left = mid+1
        # return left

        while left<=right:
            mid = left + (right - left)//2

            if arr[mid-1] <= arr[mid] and arr[mid+1]< arr[mid]:
                return mid
            elif arr[mid] >= arr[mid+1]:
                right = mid 
            else:
                left = mid+1
        return -1