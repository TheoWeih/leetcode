#https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/
#  Replace Elements with Greatest Element on Right Side

# My Solution
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        n = len(arr)
        for i in range(n-1, -1, -1):
            temp = maximum # temp = 18
            if arr[i] > maximum:
                maximum = arr[i]  # maximum = 18
            arr[i] = temp # arr[i] = 18
        return arr
            
# [17,18,5,4,6,1]    
# [17,6,6,6,1,-1] 

# Besser geschrieben
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], maximum = maximum, max(maximum, arr[i])
        return arr

# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3157/
# Move Zeroes


# Again a two pointer approach
# With slow pointing at 0

# if fast is pointing at non zero
# and slow at 0 than swap both and iterate slow 
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
            
            # iterate if nums[slow] is not 0 to keep track of zeros
            if nums[slow] != 0:
                slow += 1
        
# Sort Array By Parity
# https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3260/

# My solution, two pointer, just like move zeroes

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # slow points at odd number
        slow = 0
        for fast in range(len(nums)):
            # if fast pointer is even and slow pointer is odd swap
            if (nums[fast] % 2) == 0 and (nums[slow] % 2) != 0:
                nums[fast], nums[slow] = nums[slow] , nums[fast]
            # if new nums[slow] is even iterate slow
            # otherwise swap with slow next
            if (nums[slow] % 2) == 0:
                slow += 1
        return nums

# Other solution
class Solution:
    def sortArrayByParity(self, A):
        # use beg and end index
        beg, end = 0, len(A) - 1
        
        while beg <= end:
            # if beg is even iterate beg index
            if A[beg] % 2 == 0:
                beg += 1
            else:
            # else beg is uneven
            # swap with end and dont iterate beg
            # such that we might swap again
            # until beg is even
            # however iterate end, since end is guaranteed
            # to be odd
                A[beg], A[end] = A[end], A[beg]
                end -= 1
        return A