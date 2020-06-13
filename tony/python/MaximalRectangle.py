class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        area = 0
        m = len(matrix)
        n = len(matrix[0])
        height, left, right = [0] * n, [0] * n, [n] * n
        
        for i in range(m):
            cur_left, cur_right = 0, n  # the boundary of left and right
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                    left[j] = max(left[j], cur_left)
                else:
                    height[j] = 0
                    left[j] = 0
                    cur_left = j + 1
                
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
                
                area = max(area, (right[j] - left[j]) * height[j])
                
        return area
                    