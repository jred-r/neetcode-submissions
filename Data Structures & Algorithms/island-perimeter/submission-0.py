class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def travel(r, c):
            if r >= rows or c >= cols or r < 0 or c < 0 or grid[r][c] == 0:
                return 1

            if (r, c) in visited:
                return 0

            visited.add((r, c))

            perimeter = 0
            perimeter += travel(r + 1, c)  # >
            perimeter += travel(r - 1, c)  # <
            perimeter += travel(r, c + 1)  # V
            perimeter += travel(r, c - 1)  # ^

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return travel(r, c)

        return 0
