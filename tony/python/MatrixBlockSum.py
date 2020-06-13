class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j] + mat[i][j]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1 = max(0, i - K)
                c1 = max(0, j - K)
                r2 = min(m, i + K + 1)
                c2 = min(n, j + K + 1)
                ans[i][j] = dp[r2][c2] - dp[r2][c1] - dp[r1][c2] + dp[r1][c1]
                
        return ans