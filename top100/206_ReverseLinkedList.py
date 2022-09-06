# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            # set head = head.next to iterate 
            # prev -> curr/head -> head.next
            head = head.next
            # Keep in mind that curr.next is a pointer
            # before:
            # prev -> curr -> head
            curr.next = prev
            # after
            # prev <- curr - head
            # setting prev to curr for next iteration
            prev = curr
        return prev
            
        