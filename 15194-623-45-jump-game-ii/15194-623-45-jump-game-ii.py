class Solution:
    def jump(self, nums: List[int]) -> int:

        reach, last_pos, jumps =0,0,0

        for i in range(len(nums) - 1):
            reach = max(reach, i+nums[i])

            if i == last_pos:
                jumps += 1
                last_pos = reach
        return jumps        
        