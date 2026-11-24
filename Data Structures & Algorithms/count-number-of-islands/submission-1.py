class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        count = 0

        def bfs(row, col):
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (
                        nr < 0
                        or nr >= rows
                        or nc < 0
                        or nc >= cols
                        or (nr, nc) in seen
                        or grid[nr][nc] == "0"
                    ):
                        continue
                    seen.add((nr, nc))
                    queue.append((nr, nc))

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col] == "1":
                    seen.add((row, col))
                    bfs(row, col)
                    count += 1

        return count
