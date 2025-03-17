class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = list(word1)
        word2 = list(word2)
        merged_string = []
        while word1 or word2:

            if word1:
                merged_string.append(word1[0])
                word1 = word1[1:]
            if word2:
                merged_string.append(word2[0])
                word2 = word2[1:]
        
        if word1:
            merged_string.extend(word1)
        if word2:
            merged_string.extend(word2)
        return ''.join(merged_string)