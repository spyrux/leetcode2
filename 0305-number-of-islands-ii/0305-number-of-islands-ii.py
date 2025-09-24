from typing import List

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = [-1] * (m * n)   # -1 = water; otherwise holds parent index
        land = set()              # to skip duplicates quickly
        count = 0
        res = []

        def id(y: int, x: int) -> int:
            return y * n + x

        def find(a: int) -> int:
            # path compression
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a: int, b: int) -> None:
            nonlocal count
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra   # attach rb under ra (no rank/size heuristics)
                count -= 1        # two islands merged

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        for y, x in positions:
            # duplicate add → no change
            if (y, x) in land:
                res.append(count)
                continue
            land.add((y, x))

            i = id(y, x)
            parent[i] = i         # make land, self root
            count += 1

            for dy, dx in dirs:
                ny, nx = y + dy, x + dx
                if 0 <= ny < m and 0 <= nx < n:
                    j = id(ny, nx)
                    if parent[j] != -1:  # neighbor is land
                        union(i, j)

            res.append(count)

        return res