class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap = {}

        for x in s1:
            hashmap[x] = hashmap.get(x, 0) + 1 

        for i in range(len(s2)):
            hashmap2 = {}
            have = 0
            need = len(hashmap)
            for j in range(i, len(s2)):
                b = s2[j]
                hashmap2[b] = hashmap2.get(b, 0) + 1 

                if hashmap.get(b, 0) < hashmap2[b]:
                    break

                if hashmap.get(b, 0) == hashmap2[b]:
                    have = have + 1 

                if have == need:
                    return True 
        
        return False



        