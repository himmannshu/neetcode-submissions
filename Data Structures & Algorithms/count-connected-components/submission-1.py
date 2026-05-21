class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #n = len(edges)
        visited = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        for i in range(n):
            if i not in graph:
                graph[i] = []
        ans = 0
        def dfs(node):
            visited.add(node)
            for n in graph[node]:
                if n not in visited:
                    dfs(n)
        
        for k, v in graph.items():
            if k not in visited:
                dfs(k)
                ans += 1
        
        return ans