class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # track = defaultdict(int)

        # for start, end in intervals:
        #     track[start]+=1
        #     track[end]-=1
        
        # meeting_count = 0

        # for key in sorted(track):
        #     meeting_count+=track[key]

        #     if meeting_count > 1:
        #         return False
        # return True


        intervals.sort(key = lambda x:x[0])

        minheap = []
        prev_s = 0
        prev_e = 0
        for start, end in intervals:
            if prev_s<= start < prev_e or prev_s< end<=prev_e:
                return False
            prev_s, prev_e = start, end
        return True

           