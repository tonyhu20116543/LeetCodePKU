class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j] denotes width of submatrix with right-bottom anchor being (i,j)
        # dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        if len(matrix) == 0:
            return 0
        if len(matrix[0]) == 0:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1 if matrix[i][0] == '1' else 0
        for j in range(n):
            dp[0][j] = 1 if matrix[0][j] == '1' else 0
        
        width = 0
        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0 and matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                width = max(width, dp[i][j])
                
        return width ** 2