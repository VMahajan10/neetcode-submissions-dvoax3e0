class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            theMax = nums[i]
            for j in range(i, i + k):
                theMax = max(theMax, nums[j])
            res.append(theMax)
        
        return res
                
                

       

            


        