class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # track = defaultdict(int)

        # for i in range(len(numbers)):
        #     if numbers[i] in track:
        #         return [track[numbers[i]], i+1]
        #     else:
        #         track[target - numbers[i]] = i+1
        # return [-1, -1]

        low = 0
        high = len(numbers) - 1
        
        while low<high:
            sumval = numbers[low] + numbers[high]

            if sumval == target:
                return [low+1, high+1]
            elif sumval < target:
                low+=1
            else:
                high -= 1
        return [-1, -1]