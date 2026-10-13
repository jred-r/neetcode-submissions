class Solution:
    # brute force approach with O(n^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()
            for entry in row:
                if entry != "." and entry in seen:
                    return False
                else:
                    seen.add(entry)

        for col in range(0, 9):
            seen = set()
            for row in range(0, 9):
                entry = board[row][col]
                if entry != "." and entry in seen:
                    return False
                else:
                    seen.add(entry)

        for board_row in range(0, 9, 3):
            for board_col in range(0, 9, 3):
                seen = set()
                for row in range(board_row, board_row + 3):
                    for col in range(board_col, board_col + 3):
                        entry = board[row][col]
                        if entry != "." and entry in seen:
                            return False
                        else:
                            seen.add(entry)

        return True
