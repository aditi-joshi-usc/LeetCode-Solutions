class Solution:
    def reverse(self, x: int) -> int:
        

        # res = 0
        # isNeg = False
        # if x<0:
        #     isNeg = True
        #     x = -x

        # res = 0

        # while x>0:

        #     rem = x%10

        #     res = res*10 + rem

        #     x = x//10

        # if res >= (2**(31)-1):
        #     return 0
        # if isNeg:
        #     return res*-1
        # else:
        #     return res

        s = str(x)
        if s[0] == '-':
            s = s[1:]
            s = '-'+ s[::-1]
        else:
            s = s[::-1]
        
        x = int(s)

        if (x >= 2**(31) -1) or (x<= -2**(31)):
            return 0
     
        return x
        




