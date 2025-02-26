class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        minval = 1
        maxval = max(ribbons)
        if sum(ribbons) < k:
            return 0
        while minval<=maxval:
            midval = minval + (maxval-minval)//2
            numpossible = 0
            for r in ribbons:
                numpossible += r//midval

            if numpossible >= k:
                minval = midval + 1
            else:
                maxval = midval - 1
        return maxval