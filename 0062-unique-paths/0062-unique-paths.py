from collections import deque
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n)] for _ in range(m)]
        if m == 1 or n == 1:
            return 1
        paths[m-1][n-2], paths[m-2][n-1] = 1, 1
        queue = deque()
        visited = set()
        length = m
        width = n
        queue.append((m-1, n-2))
        queue.append((m-2, n-1))
        dirs = [(0,-1), (-1, 0)]
        while queue:
            y, x = queue.popleft()

            for dy, dx in dirs:
                if 0 <= y+dy < m and 0 <= x+dx < n and (y+dy, x+dx) not in visited:
                    queue.append((y+dy,x+dx))
                    visited.add((y+dy, x+dx))
                if 0 <= y-dy < m and 0 <= x-dx < n:
                    paths[y][x] += paths[y-dy][x-dx]
        
        return paths[0][0]
