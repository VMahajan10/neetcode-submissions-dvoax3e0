class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l = 0
        maxfreq = 0
        res = 0

        for i in range(len(s)):
            hashmap[s[i]] = hashmap.get(s[i], 0) + 1 

            maxfreq = max(maxfreq, hashmap.get(s[i]))

            while (i - l + 1) - maxfreq > k:
                hashmap[s[l]] -= 1 
                l = l + 1 
            
            res = max(res, i - l + 1)
        
        return res

            

            
        
            

            




        
        


            

    



        
        


                

        
        

            

        
                




       
                




            
            






        

        