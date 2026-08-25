class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        rows, columns = len(grid), len(grid[0])
        visited = set()


        def dfs(r, c, dist):
            if (r < 0 or c < 0 or r >= rows or c >= columns or (r, c) in visited or grid[r][c] == -1):
                return 

            visited.add((r, c))
            q.append([r, c])
            grid[r][c] = dist

            

            

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 1
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                dfs(r + 1, c, dist)
                dfs(r - 1, c, dist)
                dfs(r, c + 1, dist)
                dfs(r, c - 1, dist)
            dist += 1 

            


        