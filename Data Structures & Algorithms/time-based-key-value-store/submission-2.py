class TimeMap:

    def __init__(self):
        self.m = defaultdict(list)

        

    """ 

    stores key with val value at given timestamp
    oh i missed a key constraint
    all timestamps of set are STRICTLY increasing
    o(1)
    """ 
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value, timestamp))
        
    """ 
    returns value at key with a timestamp <= timestamp
    if multiple exist, largest timestamp to tiebreak
    if no values exist for key return ""
    o(log n)
    """ 
    def get(self, key: str, timestamp: int) -> str:
        values = self.m[key]
        l, r = 0, len(values) - 1
        candidate = ""
        while l <= r:
            mid = l + (r - l)//2
            if values[mid][1] <= timestamp:
                candidate = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return candidate
        
