class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        track = {}

        for s in strs:
            slist = ''.join(sorted(s))
            if slist in track:
                track[slist].append(s)
            else:
                track[slist] = [s]
        res =[]
        for key, val in track.items():
            res.append(val)
        return res

