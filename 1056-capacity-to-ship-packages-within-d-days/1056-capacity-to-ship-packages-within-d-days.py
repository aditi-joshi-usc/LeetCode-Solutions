class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)


        while left < right:
            mid = left + (right-left)//2
            
            currwt = 0
            ds = 0

            for wt in weights:
                if currwt+wt > mid:
                    currwt = wt
                    ds+=1
                else:
                    currwt+=wt

            if currwt>0:
                ds+=1 
                

            if ds > days:
                left = mid+1
            else:
                right = mid
        return left

