class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for a, b in prerequisites:
            adj_list[a].append(b)
        
        unseen = 0
        visiting = 1
        visited = 2

        states = [unseen]*numCourses

        def dfs(node):
            state = states[node]

            if state == visited:
                return True
            elif state == visiting:
                return False
            else:
                states[node] = visiting

                for adj in adj_list[node]:
                    if not dfs(adj):
                        return False
                states[node] = visited
                return True


        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

