# Explanation
# To know which area of the area you need to search you first need to identify which portion of the rotated
# array you are in
# Left portion: You are in the left portion of the array of nums[l] < nums[mid] which means that
# the array is sorted in increasing order from index l to mid
# Right portion: You are in the right portion if the array is sorted in increasing order from index mid to r
# Now we need to mention the subcases for left and right portions
# Left portion subcases:
# If the target is less than nums[l] or greater than nums[mid], it does not exist in the left portion and you must search right
# If the target is greater than or equal to nums[l] or less than or equal to nums[mid] you need to search the left portion
# Right portion subcases:
# If the target is less than nums[mid] or greater than nums[r], search left
# Otherwise, search right
# Not found case: Return -1 upon exiting the while loop

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l

            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]: # In left sorted portion
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else: # In right sorted portion
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1 # Target is not found

if __name__ == "__main__":
    solution = Solution()
    nums = [3,5,6,0,1,2]
    target = 4
    result = solution.search(nums, target)
    print(f'{result}')
