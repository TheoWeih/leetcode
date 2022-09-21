# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
# Find Pivot Index

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        leftsum = 0
        # enumerate counter = i, element = x
        for i, x in enumerate(nums):
            # if sum - leftsum - x equals right sum 
            # if leftsum is same as rightsum
            if leftsum == (s - leftsum - x):
                return i
            leftsum += x
        return -1


# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
# Largest Number At Least Twice of Others
# Note: Very similiar to a previous exercise
# just save index and check after getting highest and second highest element
# also enumerate comes in handy here again
# as we need the index

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1
        
        highest = -1
        highest_index = 0
        second_highest = -1
        
        for i, n in enumerate(nums):
            if n > highest:
                highest, highest_index, second_highest = n, i, highest
            elif n > second_highest:
                second_highest = n
        if highest < second_highest * 2:
            highest_index = -1
        
        return highest_index
            
            
# https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
# Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
                    
            
            
                    