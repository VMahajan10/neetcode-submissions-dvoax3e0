class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sublevel = []

        def dfs(i):
            if i == len(nums):
                res.append(sublevel.copy())
                return

            sublevel.append(nums[i])
            dfs(i + 1)
            sublevel.pop()
            dfs(i + 1)
            

        dfs(0)
        return res
        

