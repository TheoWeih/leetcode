# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur =  dummy = ListNode()
        # use cur as iterator pointing on smaller node
        while list1 and list2:
            if list1.val < list2.val:
                # setting pointer cur.next to list1 , cur -> list1
                cur.next = list1
                # iterate cur and for next iteration
                cur = cur.next 
                # prev -> cur/list1
                # iterate list1 to access next value
                list1 = list1.next
                # same as 
                # list1, cur = list1.next, list1
            else:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
                # list2, cur = list2.next, list2
        # after while one of the lists is empty, append full list to end
        if list1 or list2:
            cur.next = list1 if list1 else list2
        return dummy.next
                    