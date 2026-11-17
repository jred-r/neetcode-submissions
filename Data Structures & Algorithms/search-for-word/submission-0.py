class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def backtrack(r, c, i):
            if i == len(word):
                return True

            if (
                min(r, c) < 0  # out of bounds
                or r >= rows
                or c >= cols  # out of bounds
                or word[i] != board[r][c]  # char not equal
                or (r, c) in visited
            ):  # already visited
                return False

            visited.add((r, c))
            res = (
                backtrack(r + 1, c, i + 1)  # right
                or backtrack(r - 1, c, i + 1)  # left
                or backtrack(r, c + 1, i + 1)  # up
                or backtrack(r, c - 1, i + 1)  # down
            )
            visited.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
