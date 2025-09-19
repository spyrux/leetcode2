class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # for all 1's on the board bfs to nearest 0
        queue = []
        dist = [[float('inf') for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(0, len(mat)):
            for j in range(0, len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j,0))
                    dist[i][j] = 0

        vectors = [(0,1),(0,-1),(1,0),(-1,0)]
        while queue:
            curr = queue.pop(0)
            x = curr[0]
            y = curr[1]
            steps = curr[2]
            for dx, dy in vectors:
                if x+dx < len(mat) and x+dx >= 0 and y+dy < len(mat[0]) and y+dy >= 0 and dist[x+dx][y+dy] > steps+1:
                    queue.append(((x+dx),(y+dy),(steps+1)))
                    dist[x+dx][y+dy] = steps+1 

        
        return dist
                
        


