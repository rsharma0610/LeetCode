class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []
        for index, height in enumerate(heights):
            if not stack:
                stack.append([index, height])
            else:
                if(stack[-1][1] <= height):
                    stack.append([index, height])
                else:
                    startingIndex = index
                    while height < stack[-1][1]:
                        poppedIndex, poppedHeight = stack[-1][0], stack[-1][1]
                        maxArea = max(maxArea, (index - poppedIndex) * poppedHeight)
                        startingIndex = poppedIndex
                    
                    stack.append([startingIndex, height])
        
        for poppedIndex, poppedHeight in stack:
            maxArea = max(maxArea, (len(heights) - poppedIndex) * poppedHeight)
        
        return maxArea
    
if __name__ == "__main__":
    from typing import List  # Ensure the List type hint works
    solution = Solution()
    heights = [1, 3, 7]
    result = solution.largestRectangleArea(heights)
    print("The largest rectangle area is:", result)



