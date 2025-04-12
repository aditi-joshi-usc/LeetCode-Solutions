class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        visited = 2
        unvisited = 0
        visiting = 1

        levels = [0 for _ in range(numCourses)]

        track = defaultdict(list)
        for course, prereq in prerequisites:
            track[course].append(prereq)
        
        res = []

        def traverse(course):
            if levels[course] !=0:
                return 
            levels[course] = 1
            for pre in track[course]:
                if levels[pre] == 0:
                    traverse(pre)
                if levels[pre] !=2:
                    return
            if course not in res:
                levels[course] = 2
                res.append(course)
            
        for i in range(numCourses):
            traverse(i)
        
        if 1 in levels:
            return []
        else:
            return res
        
                
            

