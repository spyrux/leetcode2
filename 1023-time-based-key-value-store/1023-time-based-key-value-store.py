import heapq
class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_map:
            heapq.heappush(self.time_map[key], (-timestamp, value))
        else:
           self.time_map[key] = []
           heapq.heappush(self.time_map[key], (-timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        else:
            h_copy = self.time_map[key][:]
            while h_copy and timestamp < (-1*h_copy[0][0]):
                heapq.heappop(h_copy)
            return h_copy[0][1] if h_copy else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)