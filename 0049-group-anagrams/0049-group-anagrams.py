class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        track = {}

        for s in strs:
            slist = ''.join(sorted(s))
            if slist in track:
                track[slist].append(s)
            else:
                track[slist] = [s]
        return list(track.values())

        # track = defaultdict(list)

        # for s in strs:

        #     count = [0]*26
        #     for c in s:
        #         count[ord(c) - ord('a')]+=1
        #     track[tuple(count)].append(s)
        # return list(track.values()) 
