class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def backtrack(a, b):
            if b >= len(s):
                if a == b:
                    res.append(cur.copy())
                return 
            
            if self.isPali(a, b, s):
                cur.append(s[a : b + 1])
                backtrack(b + 1, b + 1)
                cur.pop()

            backtrack(a, b + 1)
        
        backtrack(0, 0)
        return res 
            

        
    def isPali(self, start: int, end: int, s: str) -> bool:
        while start < end:
            if s[start] != s[end]:
                return False
            
            start, end = start + 1, end - 1 
        
        return True 