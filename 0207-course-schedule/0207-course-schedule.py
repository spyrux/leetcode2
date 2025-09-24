class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        adj_list = {i:[] for i in range(numCourses)}


        for course, req in prerequisites:
            if course in adj_list:
                adj_list[course].append(req)
            else:
                adj_list[course] = [req]

        def dfs(course):
            if course in visited:
                return False
            if adj_list[course] == []:
                return True
            visited.add(course)
            for req in adj_list[course]:
                if not dfs(req):
                    return False
            adj_list[course] = []
            visited.remove(course)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True
            

