class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num >= self.large[0]:
            heapq.heappush(self.large, num)

        else:
            heapq.heappush(self.small, (-1 *num))


        if len(self.large) - len(self.small) > 1:
            m = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * m)
        
        elif len(self.small) - len(self.large) > 1:
            k = heapq.heappop(self.small) * -1
            heapq.heappush(self.large, k)
        

    def findMedian(self) -> float:
        m = len(self.large) + len(self.small)

        if m % 2 == 0:
            k = self.large[0] + (-1 * self.small[0])
            return k/2
        
        elif len(self.large) > len(self.small):
            return self.large[0]

        else:
            return -1 * self.small[0]


        
        