class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        fresh = set()
        seen = set()
        queue = []
        length = len(grid)
        width = len(grid[0])
        for i in range(length):
            for j in range(width):
                if grid[i][j] == 1:
                    fresh.add((i,j))
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        
        if len(fresh) == 0:
            return 0
        
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        while queue:
            y, x, minute = queue.pop(0)
            print(y,x,minute)
            minutes = minute
            for dy, dx in dirs:
                if 0 <= y+dy < length and 0 <= x+dx < width and grid[y+dy][x+dx] == 1 and (y+dy,x+dx) not in seen:
                    queue.append((y+dy,x+dx, minute+1))
                    seen.add((y+dy,x+dx))

        if seen!=fresh:
            return -1

        return minutes 
                

