class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1]*len(nums)

        prod = 1

        for i in range(len(nums)):

            answer[i] *= prod
            prod = prod*nums[i]
        

        n= len(nums)-1
        prod = 1
        while n >=0:
            answer[n] *=prod
            prod = prod*nums[n]
            n-=1
        return answer
