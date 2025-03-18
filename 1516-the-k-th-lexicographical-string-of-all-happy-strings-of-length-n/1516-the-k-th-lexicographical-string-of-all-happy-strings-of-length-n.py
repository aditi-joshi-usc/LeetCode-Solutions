class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        letters = ['a', 'b', 'c']
        def dfs(s):
            if len(s) == n:
                res.append(s.copy())
            if len(res) == k:
                return 
            if len(s) > n:
                return

            for letter in letters:
                if len(s) > 0 and letter == s[-1]:
                    continue
                s.append(letter)
                dfs(s)
                s.pop()
        dfs([])

        if len(res) >= k:
            return ''.join(res[k-1])
        else:
            return ''
     