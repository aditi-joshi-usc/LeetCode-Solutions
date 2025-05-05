class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))

        sub = []

        for env in envelopes:
            i = bisect_left(sub, env[1])
            if i == len(sub):
                sub.append(env[1])
            else:
                sub[i] = env[1]
        return len(sub)