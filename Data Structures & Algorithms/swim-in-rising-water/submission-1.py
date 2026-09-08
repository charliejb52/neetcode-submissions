class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        n = len(grid)


        def dfs(r, c, t, seen):

            if min(r, c) < 0 or max(r, c) >= n or grid[r][c] > t or (r, c) in seen:
                return False

            elif r == n - 1 and c == n - 1:
                return True

            else:
                seen.add((r, c))
                return (dfs(r + 1, c, t, seen) or
                       dfs(r - 1, c, t, seen) or
                       dfs(r, c + 1, t, seen) or
                       dfs(r, c - 1, t, seen))

        
        minh = min([num for row in grid for num in row])
        maxh = max([num for row in grid for num in row])

        for t in range(minh, maxh+1):

            if dfs(0, 0, t, set()):
                return t
        
        return -1
        
        
        

        


            



        