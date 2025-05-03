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


        # Time complexity = O(n*k log k)
        # where n is the number of strings and k is is the length of each string
        # klogk is the time for sorting

        # space complexity = O(n*k)
        # where n are the keys and k is the len of each key
        # this is worst case when there are no comman keys

        # track = defaultdict(list)

        # for s in strs:

        #     count = [0]*26
        #     for c in s:
        #         count[ord(c) - ord('a')]+=1
        #     track[tuple(count)].append(s)
        # return list(track.values()) 
