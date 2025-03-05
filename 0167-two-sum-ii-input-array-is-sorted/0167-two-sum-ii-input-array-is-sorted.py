class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        track = defaultdict(int)

        for i in range(len(numbers)):
            if numbers[i] in track:
                return [track[numbers[i]], i+1]
            else:
                track[target - numbers[i]] = i+1
        