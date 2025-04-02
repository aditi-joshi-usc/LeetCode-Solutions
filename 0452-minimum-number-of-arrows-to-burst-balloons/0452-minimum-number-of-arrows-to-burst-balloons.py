class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) <=1:
            return len(points)
        points.sort(key = lambda x:x[0])
        
        res = [points[0]]

        for i in range(1, len(points)):
            
            if points[i][0] <= res[-1][1]:
                res[-1] = [max(points[i][0], res[-1][0]), min(points[i][1], res[-1][1])]
            else:
                res.append(points[i])
        return len(res)