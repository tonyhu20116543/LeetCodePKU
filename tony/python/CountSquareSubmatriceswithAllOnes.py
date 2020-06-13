class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # dp[i][j] denotes width (the number) of submatrix with right-bottom anchor being (i,j)
        # dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        count = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i != 0 and j != 0 and matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                count += matrix[i][j]
                
        return count