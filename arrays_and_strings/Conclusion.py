# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1182/
# Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # In case k is bigger than len(nums)
        k = k % n

        # with nums[] = nums[n-k:] + nums[:n-k]
        # only pointers will be moved, which leads to the same list as the original
        nums[:] = nums[n-k:] + nums[:n-k]
        
        return nums

# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/
# Pascal's Triangle II

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 0 indexed
        pascal= [[1]*(i+1) for i in range(rowIndex+1)]
        for i in range(rowIndex+1):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal[rowIndex]
        

# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1171/discuss/38467/Very-simple-Python-solution
# Simple Python solution from discussions
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            # e.g. [1, 2, 1], zip creates two lists [0, 1, 2, 1] and [1, 2, 1, 0]
            # then perform elementwise addition
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/
# Reverse Words in a String
class Solution:
    def reverseWords(self, s: str) -> str:
        return (' '.join(reversed(s.split())))

# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1165/
# Reverse Words in a String III
class Solution:
    def reverseWords(self, s: str) -> str:
        # e.g. "Hello World" -> ["Hello", "World"]
        s = s.split()
        # reverse order of words 
        # ["Hello", "World"] -> ["World", "Hello"]
        s = s[::-1]
        # join words together to a string again
        # ["World", "Hello"] -> "World Hello"
        s = (" ".join(s))
        # reverse whole string
        # "World Hello" -> "olleH dlroW"
        s = s[::-1]
        return s

# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1173/
# Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 1
        for fast in range(len(nums)-1):
            # Remember that array is sorted in non decreasing order
            # Slow pointer points at duplicate number candidate
            # Swap slow with fast+1 if fast+1 is a new number
            # if new number (fast+1) is found swap it with slow and iterate slow
            # as now all numbers before slow are new numbers
            if nums[fast] != nums[fast+1]:
                nums[slow] = nums[fast+1]
                slow += 1   
        return slow
        
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = 0
        
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]
            
            if nums[slow] != 0:
                slow += 1
        
        
        # [1,3,12,0,0]
        #      |

        