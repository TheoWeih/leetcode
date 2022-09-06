# https://leetcode.com/problems/majority-element/

class Solution:

        
# #         # bruteforce use a dictionary and then return max
#         d = {}
#         for i in nums:
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1
#             if d[i] > len(nums)//2:
#                 return i
#         #use max function with key d.get
#         return max(d, key=d.get)
    
    
# # Use Count with Dict
#         d = Counter(nums)
    
#         return max(d, key=d.get)
    
# # Sort list and return n/2 element
#         nums.sort()
#         return nums[len(nums)//2]


    # From the discussion
    def majorityElement(self, nums):
            
            # Boyer's Moore Algorithm --> O(1) Space
            
            # We first assume that our first num is the majority element
            # So the count here is 1 as we have seen it 1 times, if the 
            # count in the end is greater than 0 we are sure that this is majority element
            # as if you take count of majority element and subtract sum of all counts of non
            # Majority element, if that count is still positive that it proves that is
            # majority element. We do not need to check count in end over here as we are 
            # sure that there exists a majority element.
            count = 1
            
            # Our Initial guess that this is the majority element
            result = nums[0]
            
            for num in nums[1:]:
                # If the next number is not same as prev
                # and count becomes 0 make this number as majority element and initialize 
                # count to 1 again else just decrease the count
                if num != result:
                    # decrease count by 1
                    count -= 1
                    # Make this element as majority element
                    if count == 0:
                        result = num
                        count = 1            
                else:
                    # This is same element as previous one.
                    count += 1
            
            return result

# Another Answer uses bit manipulation


# class Solution(object):

#     # Bit manipulation

#     # The algorithm first determines the frequency of each bit in the input array.
#     # If there is a number with a majority in the input (i.e. it makes up more than half of the input),
#     # then the frequency of all its set bits will be in the majority, and the frequency of all its unset bits will be in the minority.
#     #
#     # The majority number can be recreated from the frequency table by masking together all the majority bits.
#     # This relies on there being a majority. If there is not guaranteed to be a majority a second pass to check the result is required.
#     def majorityElement(self, nums):
#         bitFrequencyTable = [0] * 32 # Bit frequency table

#         #   Work out bit frequency
#         for num in nums:
#             for j in range(32): #  for each bit
#                 if (num >> j & 1) != 0: # is bit j set?
#                     bitFrequencyTable[j] += 1 # increment frequency

#         #  Recreate the majority number
#         res = 0
#         for i, val in enumerate(bitFrequencyTable): # for each bit
#             if val > len(nums) // 2:  # is bit i in the majority?
#                 if i == 31: # if the 31th bit if 1, it means it's a negative number
#                     res = -((1 << 31) - res)
#                 else:
#                     res |= 1 << i # mask bit i into the result
#         return res
