class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ''
        track = {}
        for letter in t:
            if letter in track:
                track[letter] += 1
            else:
                track[letter] = 1

            
        start , end = 0,0
        min_win_len = len(s)+1
        min_win_start = start
        num_char_unfound = len(t)
        while end < len(s):

            if s[end] in track:
                
                if track[s[end]] > 0:            
                    num_char_unfound-=1
                track[s[end]] -=1

            while num_char_unfound == 0:

                if end - start + 1 < min_win_len:
                    min_win_len = end - start + 1
                    min_win_start = start

                if s[start] in track:
                    track[s[start]] +=1

                    if track[s[start]] > 0:
                        num_char_unfound += 1
                start+=1
            end+=1

        if min_win_len == len(s) + 1:
            return ''
        else:
            return s[min_win_start: min_win_start + min_win_len]

