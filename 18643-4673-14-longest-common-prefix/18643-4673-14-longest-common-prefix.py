class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        ans = ""
        smallest = strs[0]
        biggest = strs[-1]
        for i in range(min(len(smallest), len(biggest))):
            if smallest[i] != biggest[i]:
                return ans
            ans+=smallest[i]
        return ans   