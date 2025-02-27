class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            left, right = 0, len(nums) -1
            first = -1
            while left<=right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    first = mid
                    right = mid-1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return first
        
        def find_second(nums, target):
            left, right = 0, len(nums) -1
            second = -1
            while left<=right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    second = mid
                    left = mid+1
                elif nums[mid] < target:
                    left = mid+1
                else:
                    right = mid-1
            return second
        
        return [find_first(nums, target), find_second(nums, target)]