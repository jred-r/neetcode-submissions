class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we need to look at each row each column and each 3*3 square.
        #maintain a set and add each element as you see them if it is already in seen then
        #it's not a valid sudoku.
       
        for row in board:
            seen = set()
            for entry in row:
                if entry == ".":
                    continue
                elif entry in seen:
                    return False
                else:
                    seen.add(entry)

       
        for col in range(0,9):
            seen = set()
            for row in range(0,9):
                entry = board[row][col]
                if entry == ".":
                    continue
                elif entry in seen:
                    return False
                else:
                    seen.add(entry)
        
        for board_row in range(0,9,3):
            for board_col in range(0,9,3):
                seen =set()
                for row in range(board_row, board_row+3):
                    for col in range(board_col, board_col+3):
                        entry = board[row][col]
                        if entry == ".":
                            continue
                        elif entry in seen:
                            return False
                        else:
                            seen.add(entry)

        return True



