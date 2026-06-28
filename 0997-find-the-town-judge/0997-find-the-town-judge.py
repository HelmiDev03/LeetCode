from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(1,n+1):
            graph[i]=[]
        for i in trust:
            graph[i[0]].append(i[1])
        townJudje = -1 
        for node in graph :
            if not graph[node] :
                townJudje = node
        for node in graph:
            if node==townJudje:
                continue
            if townJudje not in graph[node]:
                return -1
        return townJudje                       
        