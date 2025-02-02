class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings) 
        c1 = [1]*n
        c2 = [1]*n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                c1[i] = c1[i-1] +1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                c2[i] = c2[i+1] +1
        ans =0
        for x, y in zip(c1, c2):
            ans += max(x,y)
        return ans
         
