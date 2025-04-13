class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []


        def comb(start, subarray):
            if len(subarray) == k:
                res.append(subarray.copy())
                return 
            if start > n:
                return
            
            for i in range(start, n+1):
                subarray.append(i)
                comb(i+1,subarray)
                subarray.pop()
        comb(1,[])
        return res


            

