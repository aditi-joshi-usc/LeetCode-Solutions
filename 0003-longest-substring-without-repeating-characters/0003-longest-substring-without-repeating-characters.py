class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if  n<= 1:
            return n
        maxlen = 0
        left = 0
        right = 0

        while right<n:
            maxlen = max(maxlen, len(s[left:right]))
            if s[right] in s[left:right]:
                while s[right] in s[left:right] and left<right:
                    left+=1
            
            right+=1
        maxlen = max(maxlen, len(s[left:right]))
        return maxlen
        