from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            size = 1
            for nei in graph[node]:
                if not visited[nei]:
                    size += dfs(nei)
            return size

        comp_sizes = []

        for i in range(n):
            if not visited[i]:
                comp_sizes.append(dfs(i))

        res = 0
        total = 0
        for sz in comp_sizes:
            res += sz * total
            total += sz

        return res