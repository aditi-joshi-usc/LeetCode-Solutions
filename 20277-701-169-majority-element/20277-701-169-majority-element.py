class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        num_dict =defaultdict(int)

        for num in nums:
            num_dict[num] +=1
        
        n = len(nums) //2

        for key, value in num_dict.items():
            if value>n:
                return key
        
        return 0


