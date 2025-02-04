class Solution:
    def trap(self, height: List[int]) -> int:
        

        left_pointer = 0
        right_pointer = len(height) - 1

        left_max = 0
        right_max = height[right_pointer]

        water = 0

        while left_pointer < right_pointer:
            if height[left_pointer] <= height[right_pointer]:
                if left_max < height[left_pointer]:
                    left_max =  height[left_pointer]
                
                elif height[left_pointer] < left_max:
                    water += left_max - height[left_pointer]
                left_pointer += 1
            else:
                if right_max < height[right_pointer]:
                    right_max =  height[right_pointer]
                
                elif height[right_pointer] < right_max:
                    water += right_max - height[right_pointer]
                right_pointer -= 1
        return water






        