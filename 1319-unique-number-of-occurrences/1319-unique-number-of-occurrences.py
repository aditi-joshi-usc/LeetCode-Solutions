class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        track = defaultdict(int)

        for a in arr:
            track[a]+=1
        
        occured = set()

        for key, value in track.items():
            if value in occured:
                return False
            else:
                occured.add(value)
        return True
