class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def combsum(start, subarray, sumval):
            
            
            if sumval == target:
                res.append(subarray[:])
                return
            if sumval>target:
                return 
            
            for i in range(start, len(candidates)):
                subarray.append(candidates[i])
                combsum(i, subarray, sumval+candidates[i])
                subarray.pop()
        combsum(0, [], 0)
        return res
