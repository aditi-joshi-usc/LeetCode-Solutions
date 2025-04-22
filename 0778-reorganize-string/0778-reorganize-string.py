class Solution:
    def reorganizeString(self, s: str) -> str:
        pq = []

        track = {}
        for schar in s:
            if schar in track:
                track[schar] +=1
            else:
                track[schar] =1
        
        for key, value in track.items():
            pq.append((-value, key))
        
        heapq.heapify(pq)

        res = []

        while pq:
            count, char = heapq.heappop(pq)
            if res and res[-1] == char:
                if pq:
                    second_cnt, second_char = heapq.heappop(pq)
                    res.append(second_char)
                    second_cnt+=1
                    if second_cnt!=0:
                        heapq.heappush(pq, (second_cnt, second_char))
                else:
                    return ""     
            else:
                res.append(char)
                count+=1
            if count!=0:
                heapq.heappush(pq, (count, char))
        return ''.join(res)
