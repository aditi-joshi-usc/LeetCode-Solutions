class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        maxsize = 0

        track = defaultdict(int)

        for i in range(1, n+1):
            digit_sum = sum(int(d) for d in str(i))
            track[digit_sum] +=1
        maxsize = max(track.values())
        
        res = 0

        for value in list(track.values()):
            if value == maxsize:
                res+=1
        return res


        