class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        count = defaultdict(int)
        res = []

        for num in nums:
            count[num] += 1 

        for i in range(len(nums) - 1):
            count[nums[i]] -= 1 

            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1 

                target = -1 * (nums[i] + nums[j])
                if count[target] > 0:
                    theRes = [nums[i], nums[j], target]
                    if theRes not in res:
                        res.append(theRes)

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1

        return res


        







