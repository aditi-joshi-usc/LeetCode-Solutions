class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        track = {}
        memo = {}
        for key, val in replacements:
            track[key] = val
        
        i = 0

        if not text:
            return text
        
        
        return self.replacesubstring(text, track, memo)


    def replacesubstring(self, text, track, memo):
        res = []
        if '%' not in text:
            return text
        text_len = len(text)
        i=0
        while i < text_len:

            if text[i] == '%':
                j = i+1
                while j < text_len and text[j] != '%':
                    j+=1
                key = track[text[i+1:j]]
                if key not in memo:
                    memo[key] = self.replacesubstring(track[text[i+1:j]], track, memo)
                res.append(memo[key])
                i = j+1
            else:
                res.append(text[i])
                i+=1
        
        return ''.join(res)