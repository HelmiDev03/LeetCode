from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges):

        def isThereAlreadyExistingPath(u,target):
            if u==target:
                return True
            visited[u]=1
            for nei in graph[u]:
                if not visited[nei] : 
                    if isThereAlreadyExistingPath(nei, target):
                        return True
            return False    






        graph = defaultdict(list)  
        n=len(edges)
        visited=[0]*n
        for u,v in edges :
            if u-1 in graph and v-1 in graph  and isThereAlreadyExistingPath(u-1,v-1):
                return [u,v]
            graph[u-1].append(v-1)
            graph[v-1].append(u-1)   
            visited=[0]*n  