class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        track = {}

        for i, num in enumerate(nums):
            if num in track:
                if i- track[num] <= k:
                    return True
            track[num] = i
        return False