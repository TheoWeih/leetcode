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

# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
# Two Sum II - Input array is sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # two pointer solution
        l, r = 0, len(numbers)-1
        
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            # if sum is smaller than target
            # l+=1 will increase sum
            elif s < target:
                l += 1
            # if sum is bigger than target
            # r-=1 will decrease sum
            
            else:
                r -= 1
            
# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1157/
# Two-pointer Technique - Scenario II
# Sometimes, we can use two pointers with different steps to solve problems.

# https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
# Minimum Size Subarray Sum (Medium)

# Try bruteforce again