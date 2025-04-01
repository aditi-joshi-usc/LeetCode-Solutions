class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # track1 = defaultdict(int)
        # track2 = defaultdict(int)

        # for w in s:
        #     track1[w] +=1
        # for w in t:
        #     track2[w] +=1
        # return track1 == track2
        for i in s:
            if s.count(i) != t.count(i):
                return False
        return True