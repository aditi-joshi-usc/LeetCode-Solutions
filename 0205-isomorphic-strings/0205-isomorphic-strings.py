class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        track = {}
        slen  = len(s)
        tlen = len(t)
        taken = set()
        for i in range(max(len(s), len(t))):
            if i< slen and i< tlen:
                if s[i] in track:
                    if track[s[i]]!= t[i]:
                        return False
                elif t[i] in taken:
                    return False
                else:
                    taken.add(t[i])
                    track[s[i]] = t[i]
        return True