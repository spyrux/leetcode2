import heapq

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.time = 0                    # monotonic tick
        self.store = {}                  # key -> (value, version, tick)
        self.heap = []                   # (tick, key, version)

    def _touch(self, key):
        # bump timestamp & version, push new heap record
        val, ver, _ = self.store[key]
        ver += 1
        self.time += 1
        self.store[key] = (val, ver, self.time)
        heapq.heappush(self.heap, (self.time, key, ver))

    def get(self, key: int) -> int:
        if key not in self.store:
            return -1
        self._touch(key)
        return self.store[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.store:
            # update value, then touch
            _, ver, _ = self.store[key]
            self.store[key] = (value, ver, self.store[key][2])
            self._touch(key)
        else:
            if len(self.store) >= self.cap:
                # evict true LRU (skip stale heap entries)
                while self.heap:
                    t, k, ver = heapq.heappop(self.heap)
                    cur = self.store.get(k)
                    if cur and cur[1] == ver and cur[2] == t:
                        del self.store[k]
                        break
            # insert fresh
            self.time += 1
            self.store[key] = (value, 0, self.time)
            heapq.heappush(self.heap, (self.time, key, 0))