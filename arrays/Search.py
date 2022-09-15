# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
# Check if N and Its Double Exist

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # Bruteforce Method

        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         if i != j and arr[i] == (2 * arr[j]):
        #             return True
        # return False
            
        # Using collections (beats 94%)
        s = collections.Counter(arr)

        #check if there are more than one zeros
        if(s[0]>1): return True;


        for num in arr:
            # have to exclude num = 0, as one 0 would trigger it 
            # as 2*0 = 0, but we need two zeros
            if s[2*num] and num!=0:
                return True
        return False
    
# https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/
# Valid Mountain Array
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # Edge Cases where a valid mountain array is impossible
        if len(arr)<3 or arr[0]>=arr[1]:
            return False
        
        # Start with left side then with right side until 
        # arr[left+1] is smaller than arr[left]
        left, right = 0, len(arr)-1
        while left < len(arr)-1 and arr[left+1] > arr[left]:
            left += 1
        while right > 0 and arr[right-1] > arr[right]:
            right -= 1
        # Check if left and right are the same
        # or if left is 0 or right len(arr)-1
        # means that sides of the valid mountain are missing
        return left == right and left != 0 and right != len(arr)-1
			
        