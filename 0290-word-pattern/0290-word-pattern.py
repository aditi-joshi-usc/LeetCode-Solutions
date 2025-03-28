class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        track = {}
        s = s.split()
        taken = set()

        if len(s) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in track:
                if track[pattern[i]] != s[i]:
                    return False
            else:
                if s[i] in taken:
                    return False
                track[pattern[i]] = s[i]
                taken.add(s[i])
        return True