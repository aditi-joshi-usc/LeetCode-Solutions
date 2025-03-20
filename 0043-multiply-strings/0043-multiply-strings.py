class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # num1 = int(num1)
        # num2 = int(num2)

        # prod = num2 * num1
        # return str(prod)

        if num1 =='0' or num2 == '0':
            return '0'
        
        N = len(num1) + len(num2)
        res = [0]*N
        first_num = num1[::-1]
        second_num = num2[::-1]


        for place2, digit2 in enumerate(second_num):
            for place1 , digit1 in enumerate(first_num):

                num_zeroes = place1+ place2
                carry = res[num_zeroes]

                multiplication = int(digit1) * int(digit2) + carry

                res[num_zeroes] = multiplication%10
                res[num_zeroes+1] += multiplication//10
        if res[-1] == 0:
            res.pop()
        return ''.join(str(d) for d in reversed(res))
