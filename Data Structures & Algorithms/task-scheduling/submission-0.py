class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = Counter(tasks)
        maxHeap = [-x for x in m.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()
        timer = 0 

        while maxHeap or q:
            timer += 1 

            if not maxHeap:
                timer = q[0][1]

            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, timer + n])

            if q and q[0][1] == timer:
                count = q.popleft()[0]
                heapq.heappush(maxHeap, count)

        return timer
                

