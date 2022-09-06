# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Bruteforce Method using dictionary
        ## d = {} creates an empty dict
#         d = {}
#         for i in nums:
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1
        
        ## with d.items() you can access keys and values
#         for k,v in d.items():
#             if v == 1:
#                 return k


# Bruteforce using python count method
#         d = Counter(nums)
    
#         for k,v in d.items():
#             if v == 1:
#                 return k
        
                
# Optimised Version, using XOR Operation
# combined saves numbers
# 0 ^ 4 = 4, 0 4 ^ 2 = 0 4 2, 0 4 2 ^ 2 = 0 4 = 4
# not sure how that works though
        combined = 0
        for i in nums:
            combined ^= i
        return combined