class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        track = {0:0}

        sumval = 0
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                sumval-=1
            else:
                sumval +=1
            
            if sumval in track:
                maxlen = max(maxlen, i+1-track[sumval])
            else:
                track[sumval] = i+1
        
        
        return maxlen