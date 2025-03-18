class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # res = []
        # letters = ['a', 'b', 'c']
        # def dfs(s):
        #     if len(s) == n:
        #         res.append(s.copy())
        #     if len(res) == k:
        #         return 
        #     if len(s) > n:
        #         return

        #     for letter in letters:
        #         if len(s) > 0 and letter == s[-1]:
        #             continue
        #         s.append(letter)
        #         dfs(s)
        #         s.pop()
        # dfs([])

        # if len(res) >= k:
        #     return ''.join(res[k-1])
        # else:
        #     return ''

        res = []

        total_happy = 3 * (2**(n-1))
         
        
        
        left =1
        right = total_happy

        choices = 'abc'

        for i in range(n):
            curr = left
            partition_size =  (right - left +1 )//len(choices)

            for ch in choices:
                
                if k in range(curr, curr+partition_size):
                    res.append(ch)
                    left = curr
                    right = curr + partition_size - 1
                    choices = 'abc'.replace(ch, '')
                    break
                curr += partition_size
        return ''.join(res)
