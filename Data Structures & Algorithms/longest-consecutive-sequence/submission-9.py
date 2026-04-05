class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hashset = set(nums)

        for i in hashset:
            if i - 1 not in hashset:
                streak = 1 
                val = i 

                while val + 1 in hashset:
                    streak = streak + 1 
                    val = val + 1 
                
                res = max(res, streak)
        
        return res
            
        
        