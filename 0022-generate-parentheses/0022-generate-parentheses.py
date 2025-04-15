class Solution:
    def generateParenthesis(self, n: int) -> List[str]:


        
        llen = 2*n
        res = []
        def backtrack(open, close, subparan):
            if open == n and open == close:
                res.append(subparan)
                return
            if len(subparan) >llen:
                return
            

            if open < llen:
                backtrack(open+1, close, subparan+'(')
            if close < open:
                backtrack(open, close+1, subparan+')')

    
            
        backtrack(0,0, '')
        return res
            