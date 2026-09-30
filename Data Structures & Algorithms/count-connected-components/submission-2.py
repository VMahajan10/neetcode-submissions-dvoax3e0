class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #create graph to track to see which nodes are connected to other nodes 


        #traverse through the n nodes 


        #check to see if node has been visited before 

        #and if it has not append res by 1 and then place all of the nodes and its visited neighbors in the visited set.

        #return res 

        res = 0
        adj = [[] for i in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        for i in range(n):
            if i not in visited:
                q = collections.deque()
                q.append(i)
                visited.add(i)
                res += 1 
                while q:
                    x = q.popleft()
                    for nei in adj[x]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
        
        return res

                    

