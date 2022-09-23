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
                        
            
        