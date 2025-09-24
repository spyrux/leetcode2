class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        #use dsu and convert points into a number 
        parents = [-1]*(m*n)
        land = set()
        count = 0
        res = []

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        #find parent root recursively
        def find(i):
            if parents[i]!= i:
                 return find(parents[i])
            else:
                return parents[i]
        
        def union(i, j):
            nonlocal count
            ra = find(i)
            rb = find(j)
            if ra!=rb:
                parents[ra] = parents[rb]
                count -= 1
        
        for y, x  in positions:
            #y*width of row + row offset for flattening
            flat = (y*n)+x
            if (y,x) in land:
                res.append(count)
                #continue skips current loop interation and continues to the next one
                continue
            land.add((y,x))
            parents[flat] = flat
            count+=1
            for dy, dx in dirs:
                if y+dy < 0 or y+dy >= m or x+dx <0 or x+dx >=n:
                    continue
                if (y+dy,x+dx) in land:
                    union(flat, ((y+dy)*n+(x+dx)))
            
            res.append(count)
        
        return res

        



                