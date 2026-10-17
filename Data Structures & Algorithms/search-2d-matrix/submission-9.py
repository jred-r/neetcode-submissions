class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #single pass with whole matrix.
        m, n = len(matrix), len(matrix[0])
        left , right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left)//2
            row, col = mid // n, mid % n
            entry = matrix[row][col]
            if target == entry:
                return True
            elif target > entry:
                left = mid + 1
            elif target < entry:
                right = mid - 1
        return False