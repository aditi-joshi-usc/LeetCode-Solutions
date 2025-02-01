class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.split()
        
        word_len  = len(s)-1
        while word_len>=0:
            if s[word_len] != "" or s[word_len] != " ":
                return len(list(s[word_len]))
            word_len -=1
        return 0

