class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        resLen = float("infinity")

        hashmap = {}

        window = {}

        for i in t:
            hashmap[i] = hashmap.get(i, 0) + 1 

        l = 0 
        have = 0
        need = len(hashmap)
        for r in range(len(s)):
            a = s[r]
            window[a] = window.get(a, 0) + 1

            if a in hashmap and hashmap[a] == window[a]:
                have = have + 1 
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1 

                if s[l] in hashmap and window[s[l]] < hashmap[s[l]]:
                    have = have - 1 
                l = l + 1 
        

        l, r = res
        if resLen != float("infinity"):
            return s[l: r+1]
        
        else:
            return ""

                

            

        
        






        




        

                


       