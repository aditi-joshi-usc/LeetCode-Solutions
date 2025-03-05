class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
    #     isToeplitz = True
    #     for i in range(m):
    #         for j in range(n):
    #             isToeplitz = self.isTP(matrix, i, j, m, n)
    #             if not isToeplitz:
    #                 return False
        
    #     return isToeplitz

    # def isTP(self,matrix, i, j, m,n):
    #     if i>=m or j >= n:
    #         return True
    #     if i-1<0 or j-1< 0:
    #         return True
        
    #     if matrix[i][j] == matrix[i-1][j-1]:
    #         return self.isTP(matrix, i+1, j+1, m,n) and True
    #     else:
    #         return False
    
       

        for i in range(m):
            for j in range(n):
                x = i-1
                y = j-1
                if  x>=0 and  y>= 0 and matrix[x][y] != matrix[i][j]:
                    return False

        return True


    


