class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        self.track = {}

        for key, val in replacements:
            self.track[key] = val
        
        i = 0

        if not text:
            return text
        
        
        return self.replacesubstring(text)


    def replacesubstring(self, text):
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
                res.append(self.replacesubstring(self.track[text[i+1:j]]))
                i = j+1
            else:
                res.append(text[i])
                i+=1
        
        return ''.join(res)