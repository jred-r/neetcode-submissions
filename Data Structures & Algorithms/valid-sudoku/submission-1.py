class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                entry =  board[row][col]
                if entry == ".":
                    continue
                
                if entry in rows[row] or entry in cols[col] or entry in squares[(row //3, col //3)]:
                    return False
                
                rows[row].add(entry)
                cols[col].add(entry)
                squares[(row//3, col//3)].add(entry)

        return True
