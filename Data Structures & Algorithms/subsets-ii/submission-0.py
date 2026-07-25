class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        self.backtrack(0, [], nums)
        return self.res

    def backtrack(self,idx: int, cur: List[int], nums: List[int]):
        self.res.append(cur[:])

        for j in range(idx, len(nums)):
            if j > idx and nums[j] == nums[j - 1]:
                continue 

            cur.append(nums[j])
            self.backtrack(j + 1, cur, nums)
            cur.pop()

    