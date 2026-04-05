class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        hashset = set()

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l = l + 1 
            res = max(res, r - l + 1)
            hashset.add(s[r])
        
        return res


          










        