class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # i = 0
        # n = len(intervals)
        # start, end = newInterval

        # res = []
        # while i<n and intervals[i][1] < start:
        #     res.append(intervals[i])
        #     i+=1

        
        # while i<n and intervals[i][0] <= end:
        #     start = min(start, intervals[i][0])
        #     end = max(end, intervals[i][1])
        #     i+=1
        # res.append([start,end])

        # while i<n:
        #     res.append(intervals[i])
        #     i+=1
        # return res

        l = 0
        r = len(intervals) -1 

        while l<=r:
            mid = (l+r)//2

            if intervals[mid][0] < newInterval[0]:
                l = mid+1
            else:
                r =  mid-1
        intervals.insert(l, newInterval)

        res = [intervals[0]]

        for start, end in intervals:
            
          
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start,end])
        return res