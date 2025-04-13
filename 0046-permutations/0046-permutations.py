class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        nlen = len(nums)

        def perm(subarray):
            if len(subarray) == nlen and subarray not in res:
                res.append(subarray.copy())
                return
            for num in nums:
                if num not in subarray:
                    subarray.append(num)
                    perm(subarray)
                    subarray.pop()
        perm([])
        return res
