class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # track = defaultdict(int)

        # for start, end in intervals:
        #     track[start]+=1
        #     track[end]-=1
        
        # rooms = 0
        # k = 0
        
        # for key in sorted(track):
        #     rooms+=track[key]
        #     k = max(k, rooms)
        # return k
        intervals.sort(key =  lambda x : x[0])
        heap = []
        minroom = 1
        for start, end in intervals:
            
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            elif heap and heap[0] > start:
                minroom+=1
            heapq.heappush(heap, end)
        return minroom
