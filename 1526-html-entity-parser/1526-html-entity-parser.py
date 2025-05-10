class Solution:
    def entityParser(self, text: str) -> str:
        track = {
            '&quot;': '\"',
            '&apos;': '\'',
            '&amp;': '&',
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/'
        }

        # start traversing through entire string  and look for &


        # res = []
        # i=0
        # while i < len(text):

        #     if text[i] == '&':
        #         j = min(i+7, len(text))

        #         while j>i:
        #             if text[i:j] in track:
        #                 res.append(track[text[i:j]])
        #                 break
        #             j-=1
        #         if j==i:
        #             res.append(text[i])
        #             i+=1
        #         else:
        #             i = j
                
                
        #     else:
        #         res.append(text[i])
        #         i+=1
        # return ''.join(res)

        res = text

        for key in track:
            if key in text:
                res = res.replace(key, track[key])

        return res