# https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3253/


# Max consecutive ones
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        cur = 0
        for num in nums:
            if num == 1:
                cur += 1
                if cur > maximum:
                    maximum = cur
            else:
                cur = 0
        return maximum

#  Find Numbers with Even Number of Digits
#  Given an array nums of integers, return how many of them contain an even number of digits.
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # result = 0
        # for num in nums:
        #     if (len(str(num)) % 2) == 0:
        #         result += 1
        # return result
        return sum(len(str(n)) % 2 == 0 for n in nums)
        
# Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = collections.deque()
        left, right = 0, len(nums) - 1
        while left <= right:
            left, right = abs(nums[left]), abs(nums[right])
            if left > right:
                result.appendleft(left * left)
                left += 1
            else:
                result.appendleft(right * right)
                right -= 1
        return list(result)
    
    # answer = collections.deque()
    # l, r = 0, len(A) - 1
    # while l <= r:
    #     left, right = abs(A[l]), abs(A[r])
    #     if left > right:
    #         answer.appendleft(left * left)
    #         l += 1
    #     else:
    #         answer.appendleft(right * right)
    #         r -= 1
    # return list(answer)
        
