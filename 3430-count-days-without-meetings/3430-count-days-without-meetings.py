class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        res = []
        meetings.sort(key = lambda x:x[0])

        for start, end in meetings:
            if not res or res[-1][1] < start - 1:
                res.append([start, end])
            else:
                res[-1] = [min(start, res[-1][0]), max(end, res[-1][1])]
            

        for start, end in res:
            days-= (end-start+1)
        return days