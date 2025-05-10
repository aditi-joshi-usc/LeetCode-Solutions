class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        low  = 0
        high = low+10
        track = set()
        res = set()
        while high < len(s)+1:
            if s[low:high] in track:
                res.add(s[low:high])
            else:
                track.add(s[low:high])
            low+=1
            high+=1
        
        return list(res)