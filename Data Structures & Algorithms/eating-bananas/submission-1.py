class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        res = r 


        while l <= r:
            mid = (l + r) // 2

            totalCount = 0 
            for j in piles:
                totalCount += math.ceil(j/mid)
            if totalCount <= h:
                res = mid 
                r = mid - 1 
            else:
                l = mid + 1
        return res

        

        
            

        


       
       



        
            

        