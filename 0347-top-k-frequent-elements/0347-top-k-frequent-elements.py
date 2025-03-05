class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = defaultdict(int)
        for num in nums:
            if num in track: 
                track[num] += 1
            else:
                track[num] = 1


        q = []
        for key, value in track.items():
            q.append((value,key))
        
        res = heapq.nlargest(k, track, key = track.get)
        # result =  sorted(track.keys(), key = lambda x: track[x], reverse = True)[:k]
        # return result
        return res