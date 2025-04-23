class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins)>amount:
            return -1
        if amount in coins:
            return 1
        q = deque()
        visited = set()
        for coin in coins:
            q.append((1, amount-coin))
            visited.add(amount-coin)
        
        while q:
            qlen =len(q)
            for _ in range(qlen):
                cnum, cost = q.popleft()
                for coin in coins:
                    amt_left = cost - coin
                    if amt_left == 0:
                        return cnum+1
                    elif amt_left >0:
                        if amt_left not in visited:
                            q.append((cnum+1, amt_left))
                            visited.add(amt_left)
        return -1        

