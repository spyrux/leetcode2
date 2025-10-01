from collections import deque
# use deque for o(1) pop left because its a doubly linked list with o(1)
class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        visited = set()
        queue = deque()
        start = (-1, -1)
        height = len(grid)
        width = len(grid[0])
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == "*":
                    start = (i,j)
                if grid[i][j] == "#":
                    queue.append((i, j, 0))
                    visited.add((i,j))
        
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]
        while queue:
            y, x, steps = queue.popleft()
            for dy, dx in dirs:
                if 0 <= y+dy < height and 0 <= x+dx < width and (y+dy, x+dx) not in visited and grid[y+dy][x+dx] != "X":
                    if grid[y+dy][x+dx] == "*":
                        return steps+1
                    else:
                        queue.append((y+dy,x+dx, steps+1))
                        visited.add((y+dy, x+dx))
        

        return -1
            
