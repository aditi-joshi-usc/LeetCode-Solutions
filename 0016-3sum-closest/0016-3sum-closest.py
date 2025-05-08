class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        diff = float('inf')
        n = len(nums)
        for i in range(n):
            low = i+1
            high = n-1

            while low < high:
                sum = nums[i] + nums[low] + nums[high]

                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    low +=1
                else:
                    high -=1
            if diff == 0:
                return target
        return target - diff
            