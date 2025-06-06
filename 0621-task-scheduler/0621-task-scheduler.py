class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        a 1
        b 1
        c 1
        d 1


        a b c d a b  
        
        '''


        
        freq = [0] *26

        for t in tasks:
            freq[ord(t) - ord('A')] +=1
        freq.sort()
        chunk = freq[25] -1
        idle = chunk * n

        for i in range(24, -1, -1):
            idle -= min(chunk, freq[i])
        
        return len(tasks) + idle if idle>=0 else len(tasks)
        


