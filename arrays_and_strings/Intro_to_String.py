# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/
# Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carry = 0
        
        a, b = a[::-1], b[::-1]
        
        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0
                         
            total = digitA + digitB + carry
            # only adds last digit
            char = str(total % 2)
            # use char + res, to append to front 
            res = char + res
            carry = total // 2

        
        if carry:
            res = "1" + res
        return res

# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1161/
# Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/
# Longest Common Prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: 
            return ""
        shortest = min(strs, key=len)
        for i, char in enumerate(shortest):
            for other in strs:
                if other[i] != char:
                    return shortest[:i]
        return shortest
        

