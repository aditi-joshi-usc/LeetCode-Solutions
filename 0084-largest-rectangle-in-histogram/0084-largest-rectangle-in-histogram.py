class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
          
        stack = [-1]
        max_area = 0

        for i in range(len(heights)):

            while stack[-1]!=-1 and heights[i] <= heights[stack[-1]]:
                height_index = stack.pop()
                weight = i-stack[-1]-1
                max_area = max(max_area,weight*heights[height_index])
            stack.append(i)
        
        while stack[-1]!=-1:
            height_index = stack.pop()
            weight = len(heights)-stack[-1]-1
            max_area = max(max_area,weight*heights[height_index])

        return max_area