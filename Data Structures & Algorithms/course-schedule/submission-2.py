class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i] = []
        for a, b in prerequisites:
            graph[b].append(a)
        # print(graph)
        def dfs(root, visited):
            if visited[root]:
                return True
            
            visited[root] = True

            for node in graph[root]:
                if dfs(node, visited):
                    return True
            
            visited[root] = False

            return False
        
        for i in range(numCourses):
            if dfs(i, [False] * numCourses):
                return False

        return True