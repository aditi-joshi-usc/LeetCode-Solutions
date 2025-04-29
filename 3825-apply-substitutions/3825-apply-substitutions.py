class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        track = {}

        for key, val in replacements:
            track[key] = val

        if not text:
            return text
        
        
        return self.replacesubstring(text, track)


    def replacesubstring(self, text, track):
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
                res.append(self.replacesubstring(track[text[i+1:j]], track))
                i = j+1
            else:
                res.append(text[i])
                i+=1
        
        return ''.join(res)