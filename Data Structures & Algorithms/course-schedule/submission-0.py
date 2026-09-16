class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        #adjacency list to track the courses prereq associations 
        indegree = [0] * numCourses
        #array used to track the number of courses required remaining 

        for u,v in prerequisites:
            adj[v].append(u)
            #prereq attach to course in the graph
            indegree[u] += 1 
            #increment required courses by 1 

        
        q = collections.deque()
        #use deque to track current courses required 

        for n in range(numCourses):
            if indegree[n] == 0:
                #append courses with no preq into queue
                q.append(n)

        fresh = 0 
        while q:
            k = q.popleft()
            fresh += 1 
            #increment number of courses taken 
            for nei in adj[k]:
                #remove the neighbors course req counts by 1 
                indegree[nei] -= 1 
                #then check to see if any courses can be taken now
                if indegree[nei] == 0:
                    q.append(nei)

        return fresh == numCourses 
        #check to see if they are equal if not that means we have a cycle 


        



