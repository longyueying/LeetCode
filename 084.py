class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack = [-1]
        heights.append(-1)
        anw = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i-stack[-1]-1
                anw = max(anw, h*w)
            stack.append(i)
        return anw