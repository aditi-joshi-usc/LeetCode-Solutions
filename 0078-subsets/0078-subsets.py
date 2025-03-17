class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # n = len(nums)
        # def dfs(subset, index):
        #     if subset not in res:
        #         res.append(subset.copy())
        #     if index>= n:
        #         return 
            
        #     for i in range(index, n):
        #         subset.append(nums[i])
        #         dfs(subset, i+1)
        #         subset.pop()
        # dfs([], 0)
        # return res

        res = [[]]

        for num in nums:

            res += [curr + [num] for curr in res]
        return res