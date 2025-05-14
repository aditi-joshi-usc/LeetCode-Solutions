class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        track = defaultdict(list)
        count =0
        for j, num in enumerate(nums):

            for i in track[num]:
                if (i*j) %k ==0:
                    count+=1
            track[num].append(j)
        return count
