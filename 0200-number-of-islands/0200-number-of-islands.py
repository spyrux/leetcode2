class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #go thru grid and find ones to dfs, mark seen for all encountered in dfs
        width = len(grid[0])-1
        length = len(grid)-1
        seen = [[False for i in range(width+1)] for j in range(length+1)]
        num = 0

        def dfs(grid: List[List[str]], seen: List[List[str]], y, x):
            if y < 0 or y > length or x > width or x < 0 or seen[y][x] or grid[y][x] == '0':
                return
            seen[y][x] = True
            dfs(grid, seen, y+1,x)
            dfs(grid, seen, y-1,x)
            dfs(grid, seen, y,x+1)
            dfs(grid, seen, y,x-1)

        for i in range(0, length+1):
            for j in range(0, width+1):
                if grid[i][j] == '1' and seen[i][j] == False:
                    dfs(grid, seen, i, j)
                    num += 1
        return num

