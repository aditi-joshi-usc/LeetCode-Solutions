class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows<=1 or numRows>= len(s):
            return s
        row_begin, row_end = 0, numRows-1
        l = [""]*numRows
        row=0
        forward =True
        for i in range(len(s)):
            l[row]+= s[i]
            if i == row_begin or forward == True:
                row +=1
            elif row == row_end or forward == False:
                row-=1
            if row == row_begin or row == row_end:
                forward = not forward

        return ''.join(l)
