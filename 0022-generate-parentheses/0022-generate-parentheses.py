class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        def backtrack(open, close, subparan):
            if open == n and open == close:
                res.append(subparan)
                return
            if open > n or close > n:
                return
            if open < n:
                backtrack(open+1, close, subparan+'(')
            if close < open:
                backtrack(open, close+1, subparan+')')
        
        backtrack(0,0, '')
        return res
            