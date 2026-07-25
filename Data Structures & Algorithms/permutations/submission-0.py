class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res 
        
    def backtrack(self,cur: List[int], nums: List[int], truth:List[bool]):

            if len(cur) == len(nums):
                self.res.append(cur[:])
                return

            for j in range(len(nums)):
                if truth[j] == False:
                    cur.append(nums[j])
                    truth[j] = True 
                    self.backtrack(cur, nums, truth)
                    cur.pop()
                    truth[j] = False 


            