# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1183/
# Reverse String

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        
        if len(s) < 2:
            return s
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return s

# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
# Array Partition I
        
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = 0
        
        for i in range(0, len(nums) - 1, 2):
            result += min(nums[i], nums[i+1])
        return result

        # return sum(sorted(nums)[::2])

# Could also use Heap (better for memory)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        heapify(nums)
        result = 0
        while nums:

            # a will always be the smaller number, we don't care about b
            a, b = heappop(nums), heappop(nums)
            result += a

        return result