class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # word1 = list(word1)
        # word2 = list(word2)
        # merged_string = []
        # while word1 or word2:

        #     if word1:
        #         merged_string.append(word1[0])
        #         word1 = word1[1:]
        #     if word2:
        #         merged_string.append(word2[0])
        #         word2 = word2[1:]
        
        # if word1:
        #     merged_string.extend(word1)
        # if word2:
        #     merged_string.extend(word2)
        # return ''.join(merged_string)


        l1 , l2 = len(word1), len(word2)
        maxlen = max(l1,l2)
        if l1 == 0:
            return word2
        if l2 == 0:
            return word1

        p1 = 0
        p2 = 0
        ans=''
        for i in range(maxlen):

            if p1<l1:
                ans+=word1[p1]
                p1+=1
            if p2<l2:
                ans+=word2[p2]
                p2+=1
        return ans
