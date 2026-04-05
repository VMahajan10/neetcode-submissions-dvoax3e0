class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1 

        while l <= r:

            if nums[r] < nums[l]:
                l = l + 1 
            
            else:
                r = r - 1 

        return nums[l]

        