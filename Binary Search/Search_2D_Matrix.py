# Explanation
# The search space now involves two dimensions so we first need to identify which row to search in
# We can use binary search to find which row the target exists in since the rows are sorted
# If) The target is greater or equal to the first element of the row and less than or equal to the last
# element of the row then we hsould search the row
# If not, use the same binary search principles to decrease the search space
# Once the proper search row is found, perform basic binary search to see whether or not the target
# exists in the row

# Useful python tips
# using [-1] will get the last element of a list
# break can escape a loop which can make algorithms more efficient

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        searchRow = -1

        while top <= bottom:
            row = (bottom - top) // 2 + top

            if matrix[row][0] <= target and matrix[row][-1] >= target:
                searchRow = row
                break
            
            elif matrix[row][0] > target:
                bottom = row - 1
            
            else:
                top = row + 1
        
        if searchRow == -1:
            return False
        
        l, r = 0, len(matrix[searchRow])

        while l <= r:
            mid = (r - l) // 2 + l

            if matrix[searchRow][mid] == target:
                return True
            elif matrix[searchRow][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False

if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 10
    result = solution.searchMatrix(matrix, target)
    print(f'{result}')
            
