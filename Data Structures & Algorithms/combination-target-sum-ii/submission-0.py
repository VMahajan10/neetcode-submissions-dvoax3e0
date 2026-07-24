class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(idx, cur, val):
            if val == target:
                res.append(cur.copy())
                return

            for j in range(idx, len(candidates)):
                
                if j > idx and candidates[j] == candidates[j - 1]:
                    continue 

                if val + candidates[j] > target:
                    return 

                cur.append(candidates[j])
                backtrack(j + 1, cur, val + candidates[j])
                cur.pop()

            
        backtrack(0, [], 0)
        return res
