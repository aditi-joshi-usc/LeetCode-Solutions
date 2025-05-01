class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        
        res = []
        meetings.sort(key = lambda x:x[0])

        for start, end in meetings:
            if not res:
                res.append([start, end])
            elif start<=res[-1][1]:
                res[-1] = [min(start, res[-1][0]), max(end, res[-1][1])]
            else:
                res.append([start, end])


        for start, end in res:
            days-= (end-start+1)
        return days