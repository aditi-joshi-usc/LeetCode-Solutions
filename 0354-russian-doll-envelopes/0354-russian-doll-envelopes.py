class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))

        sub = []

        def binary_search(sub, h):
            left = 0
            right = len(sub) - 1

            while left<=right:
                mid = (left+right)//2

                if sub[mid] < h:
                    left  = mid+1
                else:
                    right = mid-1
            return left


        for env in envelopes:
            i = binary_search(sub, env[1])
            if i == len(sub):
                sub.append(env[1])
            else:
                sub[i] = env[1]
        return len(sub)