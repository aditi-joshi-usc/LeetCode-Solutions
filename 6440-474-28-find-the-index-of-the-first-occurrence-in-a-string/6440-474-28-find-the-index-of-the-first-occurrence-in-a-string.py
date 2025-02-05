class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack == needle:
            return 0
        needle_len = len(needle)
        hay_len = len(haystack) - needle_len+1
        if needle_len> len(haystack):
            return -1
        
        for i in range(hay_len):
            if needle == haystack[i:i+needle_len]:
                return i 
            
        return -1