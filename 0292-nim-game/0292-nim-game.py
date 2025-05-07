class Solution:
    def canWinNim(self, n: int) -> bool:
        
        # memo ={}

        # def dp(curr, yourTurn):
        #     if curr > n:
        #         return False
            
        #     if curr == n:
        #         return not yourTurn
        #     if (curr, yourTurn) in memo:
        #         return memo[(curr, yourTurn)]
        #     if yourTurn:
        #         res = (dp(curr+1, not yourTurn) or dp(curr+2, not yourTurn) or dp(curr+3, not yourTurn))
        #     else:
        #         res = (dp(curr+1, not yourTurn) and dp(curr+2, not yourTurn) and dp(curr+3, not yourTurn))
        #     memo[(curr, yourTurn)] = res
        #     return res

        # return dp(0, True)

        return n%4 !=0