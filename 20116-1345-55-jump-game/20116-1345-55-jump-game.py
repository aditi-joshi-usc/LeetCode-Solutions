class Solution:
    def canJump(self, nums: List[int]) -> bool:

        can = 0

        for num in nums:
            if can<0:
                return False
            elif num>can:
                can = num
            can-=1
        
        return True

            
        
        