from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # create 2 queue's for both pacific and atlantic
        pacific_queue = deque()
        atlantic_queue = deque()
        # create 2 sets to store coordinates,
        # this was we can cut down, extra processing.
        pacific_seen = set()
        atlantic_seen = set()

        # fill the top and bottom rows for both pacific and atlantic
        for col in range(cols):
            entry = (0, col)
            pacific_queue.append(entry)
            pacific_seen.add(entry)
            entry = (rows - 1, col)
            atlantic_queue.append(entry)
            atlantic_seen.add(entry)

        # fill the left and right columns for both pacific and atlantic
        # this will add the corners again, but since we have a set, we will not
        # be reprocessing the same coordinates.

        for row in range(rows):
            entry = (row, 0)
            pacific_queue.append(entry)
            pacific_seen.add(entry)
            entry = (row, cols - 1)
            atlantic_queue.append(entry)
            atlantic_seen.add(entry)

        def bfs(queue, seen):
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

        bfs(pacific_queue, pacific_seen)
        bfs(atlantic_queue, atlantic_seen)

        return list(pacific_seen & atlantic_seen)
