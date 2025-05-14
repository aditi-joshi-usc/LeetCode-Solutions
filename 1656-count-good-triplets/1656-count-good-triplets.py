class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        res=0
        llen = len(arr)
        for i in range(llen):
            for j in range(i+1, llen):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, llen):
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res+=1
            
        return res