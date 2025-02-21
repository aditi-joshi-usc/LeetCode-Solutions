class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        n = len(num)
        maxInd = n-1
        indx1 = -1
        indx2 = -1

        for i in range(n-2, -1, -1):
            if num[i] > num[maxInd]:
                maxInd = i
            elif num[i] < num[maxInd]:
                indx1 = i
                indx2 = maxInd
            
        
        if indx1 !=-1 and indx2 != -1:
            temp = num[indx1]
            num[indx1] = num[indx2]
            num[indx2] = temp
        return int(''.join(num))