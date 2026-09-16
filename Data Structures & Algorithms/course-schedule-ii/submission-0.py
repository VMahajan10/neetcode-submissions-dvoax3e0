class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses 

        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u] += 1 

        q = collections.deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)


        fresh = 0
        res = []
        while q:
            k = q.popleft()
            res.append(k)
            fresh += 1 
            for nei in adj[k]:
                indegree[nei] -= 1 
                if indegree[nei] == 0:
                    q.append(nei)

        if fresh == numCourses:
            return res

        else:
            return []





        