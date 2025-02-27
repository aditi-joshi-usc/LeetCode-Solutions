class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minheap =[]

        for x,y in points:
            dist = (x)**2 + (y)**2

            minheap.append((dist, (x, y)))


        heapq.heapify(minheap) 

        res = []
        for i in range(k):
            res.append(heappop(minheap)[1])
            
        return res