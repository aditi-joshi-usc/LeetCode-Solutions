class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        def find_parent(p, num):
            if p[num] == -1:
                return num
            return find_parent(p, p[num])
        
        logs.sort(key = lambda x: x[0])

        p = [-1]* n
        count = n


        for log in logs:
            if find_parent(p,log[1]) != find_parent(p,log[2]):
                p[find_parent(p, log[1])] = log[2]
                count -=1
            if count == 1:
                return log[0]
        return -1