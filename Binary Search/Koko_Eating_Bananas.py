# Explanation
# Use binary search algorithm because we want to find the minimum amount of bananas that can be consumed an
# hour that still results in the piles of bananas being consumed in h hours
# The left will be set to 1 because the minimum amount of bananas that can be consumed an hour will be 1
# The right will be max piles since the max amount of bananas that need to be consumed an hour is the max number of bananas
# that exists in a pile in the piles array because only one pile can be eaten from each hour
# Peform binary search the usual way, calculating the middle point between left and right and then
# perform a for loop through the piles array to determine if the bananas per hour consumption rate
# is sufficient in completeing all piles in h time
# If it is: Move left to mid - 1 because we want to see if there exists a smaller value of bananas/hour which
# works
# Else: Move left to mid + 1 because we need to up our hourly consumption to clear the piles
import math 
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)

        res = 0

        while l <= r:
            k = (r - l) // 2 + l # Eating speed per hour

            #Perform a for loop to see how many hours it will take at this eating speed to eat all the piles
            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / k)

            if time <= h:
                res = k
                r = k - 1
            
            else:
                l = k + 1
        
        return res

if __name__ == "__main__":
    solution = Solution()
    piles = [25,10,23,4]
    h = 4
    result = solution.minEatingSpeed(piles, h)
    print(f'{result}')
                    
            
            
        
