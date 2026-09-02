class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0 
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        res = 0 

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1 

                if grid[r][c] == 2:
                    q.append([r, c])


        while fresh > 0 and q:
            for i in range(len(q)):
                x,y = q.popleft()
                directions = [[1,0], [-1,0], [0, 1], [0, -1]]
                for a,b in directions:
                    dx = x + a
                    dy = y + b 

                    if (0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1):
                        grid[dx][dy] = 2
                        q.append([dx, dy])
                        fresh -= 1 
            res += 1 

        return res if fresh == 0 else -1


