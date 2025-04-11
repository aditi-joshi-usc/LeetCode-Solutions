class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        power = 31

        while n:
            res += (n & 1) << power
            power -= 1
            n = n >> 1
        return res