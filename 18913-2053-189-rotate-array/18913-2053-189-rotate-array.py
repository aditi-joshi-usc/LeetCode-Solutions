class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        list_len = len(nums)
        k  = k % list_len

        rotated = [0]*list_len
 
        for i in range (list_len):
            rotated[(i+k)%list_len] = nums[i]
        
        for i in range(list_len):
            nums[i] = rotated[i]

