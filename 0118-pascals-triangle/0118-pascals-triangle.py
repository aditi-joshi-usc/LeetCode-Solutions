class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[0] * n for n in range(1, numRows+1)]
        

        for i in range(numRows):
            res[i][0] = 1
            res[i][i]=1

            for j in range(1, i):
                if i>1:
                    res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
        



