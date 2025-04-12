class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a,b), val in zip(equations, values):
            graph[a].append((b,val))
            graph[b].append((a, 1/val))
        
        def dfs(curr, target, visited, curr_prod):
            if curr == target:
                return curr_prod
            visited.add(curr)

            for next, val in graph[curr]:
                if next not in visited:
                    ans = dfs(next, target, visited, curr_prod*val)
                    if ans != -1.0:
                        return ans
            return -1.0

        res = []
        for start, end in queries:
            if start not in graph or end not in graph:
                res.append(-1.0)
            else:
                res.append(dfs(start, end, set(), 1.0))
        return res
