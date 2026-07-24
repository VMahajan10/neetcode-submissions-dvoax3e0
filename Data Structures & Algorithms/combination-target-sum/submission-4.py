class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(idx, cur, val):

            if val == target:
                res.append(cur.copy())
                return

            for j in range(idx, len(nums)):
                if val + nums[j] > target:
                    return 

                cur.append(nums[j])
                backtrack(j, cur, val + nums[j])
                cur.pop()
        
        backtrack(0, [], 0)
        return res

        