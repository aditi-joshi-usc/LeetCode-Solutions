class Solution:
    def find_h(self,h, nums):
        if h <= 0:
            return 0
        count=0
        for num in nums:
            if num>=h:
                count+=1
            if count == h:
                return h
        
        return self.find_h(h-1, nums)



    def hIndex(self, citations: List[int]) -> int:

        n = len (citations)

        return self.find_h(n, citations)


        