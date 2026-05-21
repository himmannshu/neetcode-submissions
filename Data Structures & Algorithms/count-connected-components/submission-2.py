# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         #n = len(edges)
#         visited = set()
#         graph = defaultdict(list)
#         for a, b in edges:
#             graph[a].append(b)
#             graph[b].append(a)
#         for i in range(n):
#             if i not in graph:
#                 graph[i] = []
#         ans = 0
#         def dfs(node):
#             visited.add(node)
#             for n in graph[node]:
#                 if n not in visited:
#                     dfs(n)
        
#         for k, v in graph.items():
#             if k not in visited:
#                 dfs(k)
#                 ans += 1
        
#         return ans


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)

        res = 0
        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                res += 1
        return res