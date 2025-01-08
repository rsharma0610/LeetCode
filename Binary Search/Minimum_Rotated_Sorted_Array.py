# Explanation
# In a rotated sorted array, you can still perform binary search by leveraging the pivot
# The pivot is the point in the rotated array where it goes from increasing to decreasing
# For example, [4, 5, 6, 1, 2, 3]
# The pivot occurs at [..., 6, 1, ....] because the array goes form increasing to decreasing
# This is important because it helps us dteermine where to search for the minimum in the rotated array
# If the mid index is greater than the right index, it means that the pivot exists in the search space to the right
# of the mid index so we search right
# Otherwise, we are currently placed on the minimum(pivot) or we need to search left

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        res = float('inf')

        while l <= r:
            mid = (r - l) // 2 + l

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                res = min(res, nums[mid])
                r = mid - 1
        
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [4,5,0,1,2,32]
    result = solution.findMin(nums)
    print(f'{result}')