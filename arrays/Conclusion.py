# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/
# Height Checker

# My solution
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        result = 0
        
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                result += 1
        return result
        
# Leaner solution
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))

# Optimal solution uses Counting Sort and is O(n)
#https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3228/discuss/347368/Easy-Python-O(n)-Let's-step-through-the-algorithm
class Solution:
        # O(n log n) because of sorted
#         expected = sorted(heights)
#         result = 0
        
#         for i in range(len(heights)):
#             if heights[i] != expected[i]:
#                 result += 1
#         return result
    
    # return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))
        
# O(n) Counting Sort // O(4n)
    def heightChecker(self, heights: List[int]) -> int:
        max_nr = max(heights)
        # initialize frequency array with 0's
        count = [0] * (max_nr + 1)
        # get frequencies
        for number in heights:
            count[number] += 1
        # create a sumcount array
        sumcount = [0] * (max_nr + 1)
        for index, number in enumerate(count[1:],start=1):
            sumcount[index] = number + sumcount[index-1]
        # sumcount determines the index in sorted array
        # create output array
        output = [0] * len(heights)
        # loop backwards starting with last element for stable sort
        for p in range(len(heights)-1,-1,-1):
            output[sumcount[heights[p]]-1] = heights[p]
            sumcount[heights[p]] -= 1
		# return the difference compared to original array
        result = 0
        for index, number in enumerate(heights):
            if number != output[index]:
                result += 1
        return result






# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/
# Find All Numbers Disappeared in an Array
# Negate the corresponding index of the number found


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            # we check nums[i] and negate the value in the corresponding index
            # (have to use abs(nums[i]) as this value could already be negative
            # and use -1, so we wont get an overflow
            # as actual numbers are from 1-n, and actual index and size of array is 0-n-1
            # if we got n, we can access nums[n] for example
            temp = abs(nums[i]) - 1
            # if nums[temp] is already negative, we dont do anything
            if nums[temp] > 0:
                nums[temp] *= -1
                
            res = []
        for count, value in enumerate(nums):
            if value > 0:
                # before we matched a number to nums[i] - 1 index
                # to avoid overflow in case of n
                # now we have to add the +1 again
                res.append(count+1)
        return res
            
            
# https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3231/
#  Third Maximum Number