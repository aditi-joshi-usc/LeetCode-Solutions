class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        track = defaultdict(int)

        if not nums:
            return None
        for num in nums:
            track[num] +=1
        index = 0
        for i in range(track[0]):
            nums[index] = 0
            index+=1
        for i in range(track[1]):
            nums[index] = 1
            index+=1
        for i in range(track[2]):
            nums[index] = 2
            index+=1

    
        