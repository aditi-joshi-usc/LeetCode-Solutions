class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        track = defaultdict(int)

        for start, end in intervals:
            track[start]+=1
            track[end]-=1
        
        meeting_count = 0

        for key in sorted(track):
            meeting_count+=track[key]

            if meeting_count > 1:
                return False
        return True
