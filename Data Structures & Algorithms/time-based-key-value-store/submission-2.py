class TimeMap:

    def __init__(self):
        self.keyStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
            #Create empty list if this is the first time key is called 
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyStore.get(key, [])

        l = 0
        r = len(values) - 1 
        res = ""

        while l <= r:
            mid = (l + r)//2

            if values[mid][1] <= timestamp:
                res = values[mid][0] 
                l = mid + 1 

            else:
                r = mid - 1 

        
        return res 

        
