class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_dict = {
            '1':'',
            '2':'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result=[]
        def dfs(digits, digit_dict, digit, subval):
            if len(digits) <= digit:
                result.append(''.join(subval.copy()))
                return
            
            for val in digit_dict[digits[digit]]:
                subval.append(val)
                dfs(digits,digit_dict,digit+1, subval)
                subval.pop()

        if len(digits) < 1:
            return []
        dfs(digits,digit_dict, 0, [])
        return result