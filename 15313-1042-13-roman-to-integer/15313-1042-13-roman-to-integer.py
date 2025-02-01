class Solution:
    def romanToInt(self, s: str) -> int:
        
        nums = {
            "I" : 1,
            "V" : 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M" : 1000
        }
        
        s1 = list(s)
        answer = [0] * len(s1)

        for i in range(len(s1)):
            if i == 0:
                answer[i] = nums[s1[i]]

            else:
                answer[i] = nums[s1[i]]
                if answer[i] > answer[i-1]:
                    answer[i-1] = -1 * answer[i-1]
        sum_ans = 0
        for ans in answer:
            sum_ans+= ans
        return sum_ans


