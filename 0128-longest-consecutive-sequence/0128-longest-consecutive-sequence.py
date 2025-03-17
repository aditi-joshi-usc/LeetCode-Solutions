class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0


        numset = set(nums)

        for num in numset:
            if num-1 not in numset:
                curr_len = 1

                while num +1 in numset:
                    num+=1
                    curr_len+=1
                maxlen = max(maxlen, curr_len)
        return maxlen