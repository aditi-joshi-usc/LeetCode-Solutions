class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        l = 0
        r = 0
        map_dict={}
        w_len = len(word)
        a_len = len(abbr)
        while r < a_len and l < w_len:
            skip = 0
            if abbr[r] == word[l]:
                r+=1
                l+=1
                
            elif abbr[r] == "0":
                return False
            elif abbr[r].isnumeric():
                while r< a_len and abbr[r].isnumeric():
                    skip = int(abbr[r]) + skip*10
                    r+=1
                l+=int(skip)
            else:
                return False
        return r == a_len and l == w_len
