class Solution:
    def addDigits(self, num: int) -> int:
        '''        

                38
                3 + 8 = 11
                1+1 = 12

                456
                15
                6


                12334
                13
                68768
                35
                8


                45
                9
        '''

        if num ==0:
            return num
        # numlist = []
        # temp = num

        # while temp!=0:
        #     numlist.append(temp%10)
        #     temp = temp//10
        # if len(numlist) == 1:
        #     return num
        # while len(numlist) > 1:
        #     temp = sum(numlist)
        #     numlist = []
        #     while temp!=0:
        #         numlist.append(temp%10)
        #         temp = temp//10

        # return numlist[0]
        return num % 9 or 9