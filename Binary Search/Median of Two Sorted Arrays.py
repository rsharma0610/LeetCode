# Explanation
# We want to provide an algorithm of O(n + m) so we employ binary search
# The alogirthm revolves of around building the correct left partition of the arrays without actually combining them
# We do this by first calculating how many elements should be in the left partition:
# (len(A) + len(B)) // 2
# Next, we set up binary search for the smaller of the two arrays 
# We can do while True instead of l <= r because there is guarenteed to be a median
# So we calculate the mid index, or the right most index of the left partition of array A
# To get the right most index of the left parition of array B we can just do half - i - 2
# We do minus 2 because arrays are indexed starting at 0, so in two array we are missing two
# Then using the indices we calculate:
# Aleft, Aright, Bleft, Bright
# If Aleft is less than or equal to Bright and Bleft is less than or equal to Aright, we have found the median
# Otherwise update as typcial in binary search:
# If Aleft is greater than Bright, it means that the left partition of array A needs to be reduced, i = r - 1
# If Bleft is greater than Aright, it means that Bleft is too large and we need to increase the left parition
# of array A which in turn reduces the left partition of array B

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2

        half = (len(A) + len(B)) // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (r - l) // 2 + l
            j = half - i - 2

            ALeft = A[i] if i >= 0 else float('-infinity')
            ARight = A[i + 1] if (i + 1) < len(A) else float('infinity')
            BLeft = B[j] if j >= 0 else float('-infinity')
            BRight = B[j + 1] if (j + 1) < len(B) else float('infinity')

            if ALeft <= BRight and BLeft <= ARight:
                if (len(A) + len(B)) % 2 != 0: # The combined array is of odd length
                    return min(ARight, BRight)
                
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2

            elif ALeft > BRight: # The rightmost element of A's left partition is greater than the leftmost element of B's right partition
                r = i - 1

            else:
                l = i + 1

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,3]
    nums2 = []
    result = solution.findMedianSortedArrays(nums1, nums2)
    print(f'The median is {result}')

                
