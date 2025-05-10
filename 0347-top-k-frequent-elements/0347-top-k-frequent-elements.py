class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ''' 
        brute force:
        sort the arr and return the 1st k elements
        time complexity : O(nlogn)


        minheap:
        push into the minheap and return k popped elements
        time complexity for this  = O(n)
        because heapify is done in linear time
        heappop - O(logk) where k < n
        '''
        track=defaultdict(int)

        for num in nums:
            track[num]+=1
        minheap =[]
        for key, value in track.items():
            minheap.append((-value,key))


        

        heapq.heapify(minheap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res

