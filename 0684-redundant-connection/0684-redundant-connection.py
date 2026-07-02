from collections import defaultdict
import copy 
class Solution:
    def findRedundantConnection(self, edges):
        def hasCycle (graph):
            def dfs(node , parent):
                visited[node]=1
                for nei in graph[node]:
                    if not visited[nei] :
                        if dfs(nei,node):
                            return True
                    elif nei != parent :
                        return True
                return False        

            n=len(edges)
            visited=[0]*n    
            for node in graph:
                if not visited[node] and dfs(node,None):
                    return True
            return False    


        graph = defaultdict(list)  
        for edge in edges :
            graph[edge[0]-1].append(edge[1]-1)
            graph[edge[1]-1].append(edge[0]-1)
        ans=[]
        for removedEdge in edges:
            newgraph = copy.deepcopy(graph)
            newgraph[removedEdge[0]-1].remove(removedEdge[1]-1)
            newgraph[removedEdge[1]-1].remove(removedEdge[0]-1)
            if not hasCycle(newgraph):
                ans.append(removedEdge)
        return ans[-1] 