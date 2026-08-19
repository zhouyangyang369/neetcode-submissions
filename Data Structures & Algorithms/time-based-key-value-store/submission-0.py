class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        else:
            l = 0
            r = len(self.data[key]) - 1
            ans = ''
            while l<=r:
                mid = (l+r)//2
                time = self.data[key][mid][1]
                value = self.data[key][mid][0]
                if time <= timestamp:
                    ans = value
                    l = mid + 1
                else:
                    r = mid - 1
            return ans
