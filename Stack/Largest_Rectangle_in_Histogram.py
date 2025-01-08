# Explanation
# For each height, we want to see much it can be expanded in either direction
# The expansion to the left will be handled by pushing the starting index along with the height onto the stack
# So there are two scenarios:
# 1) If the current height is greater than the height of th bar on top of the stack,
# push the current bar onto the stack because it does not impede the rightward expansion of the bar on top of 
# the stack
# 2) If the height of the bar if less than the height of the bar on top of the stack, then it will impede
# the rightward expansion of the bar so then the total area that can be produced by the bar on top of the
# stack is known and it can be calculated by popping it off the stack and multiplying it's height by
# the current index subtracted by the popped bar's index
# As long as the current bar is lesser in height than the bar on top of the stack then the stack can be
# popped from, when the current bar is pushed onto the stack, it's index can be set to the last bar that was 
# popped from the stack because if it is shorter than the bar's being popped from the stack then,
# the bar can expand it's area leftward as well
# At the end of the process, it is possible that elements still remain in the stack, which would mean that
# they did not encounter a bar lesser in height to their right
# Simply pop these items and calculate their area by heigth * lenght of the heights array - their index
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
                    while stack and height < stack[-1][1]:
                        poppedIndex, poppedHeight = stack[-1][0], stack[-1][1]
                        maxArea = max(maxArea, (index - poppedIndex) * poppedHeight)
                        startingIndex = poppedIndex
                        stack.pop()
                    
                    stack.append([startingIndex, height])
        
        for poppedIndex, poppedHeight in stack:
            maxArea = max(maxArea, (len(heights) - poppedIndex) * poppedHeight)
        
        return maxArea
    
if __name__ == "__main__":
    from typing import List  # Ensure the List type hint works
    solution = Solution()
    heights = [7,1,7,2,2,4]
    result = solution.largestRectangleArea(heights)
    print("The largest rectangle area is:", result)



