class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        if len(A) == 1:
            return A[0][0]
        
        n = len(A)
        min_sum = float('inf')
        for i in range(1, n):
            for j in range(n):
                c1 = 0 if j - 1 < 0 else j - 1
                c2 = j if j + 1 == n else j + 1
                A[i][j] += min(A[i - 1][j], A[i - 1][c1], A[i - 1][c2])
                
                if i == n - 1:
                    min_sum = min(min_sum, A[i][j])
        
        return int(min_sum)