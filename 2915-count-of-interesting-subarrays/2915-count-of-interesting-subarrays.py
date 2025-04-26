class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        track = defaultdict(int)
        track[0] = 1
        res = 0
        cnt = 0

        for num in nums:
            if num % modulo == k:
                cnt +=1
            
            target = (cnt - k) % modulo
            res+= track[target]

            track[cnt % modulo] +=1
        return res
            