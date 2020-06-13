class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        if len(arr) == 1:
            return arr[0][0]
        
        def get_min(arr):
            min_val, min_idx = arr[0], 0
            for i in range(len(arr)):
                if arr[i] < min_val:
                    min_val = arr[i]
                    min_idx = i
            return min_val, min_idx

        def get_sec_min(arr, min_idx):
            sec_min_val, sec_min_idx = float('inf'), 0
            for i in range(len(arr)):
                if i == min_idx:
                    continue
                if arr[i] < sec_min_val:
                    sec_min_val = arr[i]
                    sec_min_idx = i
            return int(sec_min_val), sec_min_idx

        n = len(arr)
        min_sum = float('inf')
        for i in range(1, n):
            min1, idx1 = get_min(arr[i - 1])  # find min
            min2, _ = get_sec_min(arr[i - 1], idx1)  # find second min
            
            for j in range(n):
                min_val = min1 if j != idx1 else min2  # key point, if min val is not in the same col as current element, get min val. otherwise, get second min val
                arr[i][j] += min_val

                if i == n - 1:
                    min_sum = min(min_sum, arr[i][j])
                
        return int(min_sum)
                        
                    