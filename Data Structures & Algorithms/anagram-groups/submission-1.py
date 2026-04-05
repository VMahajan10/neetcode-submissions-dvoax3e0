class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in strs:
            a = ''.join(sorted(i))
            hashmap[a].append(i)
        return list(hashmap.values())


            


            




        