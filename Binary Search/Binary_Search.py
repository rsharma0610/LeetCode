# Explanation
# Binary Search is a foundational algorithm 
# First get the left index, then the right index
# Calculate the middle point of these two indices by performing (right - left) // 2 + left
# This method of calculating the middle point is used to avoid overflow issues in the case of very large
# indcies 
# Then if target is less than the middle index, set right pointer to one before the middle index
# If target is greater than middle index, set left to one after the middle index
# If target is found, return
# The whole idea of binary search is cutting the search area in half each iteration while results in
# O(log(n)) runtime
# Binary search is only possible on sorted arrays or rotated arrays 

class Solution:
    def binarySearch(self, nums: list[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r - l) // 2 + l

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return l if nums[l] == target else -1
    
if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,2,4,6,8]
    target = 4
    result = solution.binarySearch(nums, target)
    print(f'The target was found at index {result}')
