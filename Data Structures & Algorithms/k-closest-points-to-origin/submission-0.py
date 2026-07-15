class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for x,y in points:
            dist = -(x**2 + y**2)
            res.append([dist, (x, y)])

        heapq.heapify(res)

        while len(res) > k:
            heapq.heappop(res)

        theRes = []
        for i in range(len(res)):
            m = res[i]
            theRes.append(m[1])
        
        return theRes