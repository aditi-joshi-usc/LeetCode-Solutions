class Solution:
    def customSortString(self, order: str, s: str) -> str:
        track = defaultdict(int)
        
        for char in s:
            if char in order:
                track[char]+=1
        
        res = ''
        for char in order:
            res += char * track[char]
        
        for char in s:
            if char not in track:
                res += char
        return res
                