class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for i,cnt in hashmap.items():
            freq[cnt].append(i)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for x in freq[i]:
                res.append(x)

                if len(res) == k:
                    return res
        

                

            



        

        

        


        



        