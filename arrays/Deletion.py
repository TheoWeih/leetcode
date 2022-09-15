# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3247/
# Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return slow
    
# [2,2,3,3]
# 3

# slow = 2
# fast = 3

# Slow Pointer vs fast pointer approach


# https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/
# remove duplicates
# only works since array is sorted in a non-decreased order
# first element is always unique

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for fast in range(len(nums)-1):
            if nums[fast] != nums[fast+1]:
                nums[slow] = nums[fast+1]
                slow += 1
        return slow
        
# [1,2,2]
# slow = 2

# Remove Element
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3575/
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # slow points at nums[i] == val
        # nums[slow] next target to be swapped if nums[fast] != val
        # since slow pointer walks slower
        # this means that we swap nums[fast] != val
        # to the front
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return slow
    