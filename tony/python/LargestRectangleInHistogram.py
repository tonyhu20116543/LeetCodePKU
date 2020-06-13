class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0
        
        area = 0
        s = []
        heights.append(0)  # to include the last element by append
        for i in range(len(heights)):
            while len(s) != 0 and heights[s[-1]] >= heights[i]:
                idx = s.pop()
                width = i if len(s) == 0 else i - s[-1] - 1  # be careful here
                area = max(area, heights[idx] * (i if len(s) == 0 else i - s[-1] - 1))
            s.append(i)
                
        return area