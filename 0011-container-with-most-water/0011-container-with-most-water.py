class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        maxarea = 0

        l = 0
        r = len(height)-1

        while l<r:
            width = r-l
            length = min(height[l], height[r])
            maxarea = max(maxarea, width*length)
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        return maxarea
        