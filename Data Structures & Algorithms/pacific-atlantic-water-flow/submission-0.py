from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacific_q = deque()
        atlantic_q = deque()

        pacific_seen = set()
        atlantic_seen = set()

        for c in range(cols):
            pacific_q.append((0, c))
            pacific_seen.add((0, c))

            atlantic_q.append((rows - 1, c))
            atlantic_seen.add((rows - 1, c))

        for r in range(rows):
            pacific_q.append((r, 0))
            pacific_seen.add((r, 0))

            atlantic_q.append((r, cols - 1))
            atlantic_seen.add((r, cols - 1))

        def bfs(queue, seen):
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                row, col = queue.popleft()

                for dr, dc in directions:
                    nr, nc = row + dr, col + dc

                    if (
                        nr < 0
                        or nr >= rows
                        or nc < 0
                        or nc >= cols
                        or (nr, nc) in seen
                        or heights[nr][nc] < heights[row][col]
                    ):
                        continue

                    seen.add((nr, nc))
                    queue.append((nr, nc))

        bfs(pacific_q, pacific_seen)
        bfs(atlantic_q, atlantic_seen)

        return list(pacific_seen & atlantic_seen)
