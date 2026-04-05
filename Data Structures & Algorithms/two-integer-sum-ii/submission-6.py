class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        res = []
        for i in range(len(numbers)):
            newTarget = target - numbers[i]
            if newTarget in hashmap: 
                res = [hashmap.get(newTarget) + 1 , i + 1]
                return res
            hashmap[numbers[i]] = i 
        
        if len(res) == 0:
            return []

        
        
                



        
                

            
        
