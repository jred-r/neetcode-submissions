class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        grid = defaultdict(set)

        for row in range(9):
            for col in range(9):
                entry = board[row][col]
                if entry == ".":
                    continue
                
                if entry in rows[row] or entry in cols[col] or entry in grid[(row//3, col//3)]:
                    return False
                else:
                    rows[row].add(entry)
                    cols[col].add(entry)
                    grid[(row//3, col//3)].add(entry)

        return True

        