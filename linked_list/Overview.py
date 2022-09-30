# https://leetcode.com/explore/learn/card/linked-list/

# Singly Linked List and Doubly Linked List



# https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/
# Design Linked List

# Need Class Node with attributes val and next
# And LinkedList class with attributes head and size

class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self, val):
        self.head = None
        self.size = 0
        
    def get(self, index: int) -> int:
        if index < 0:
            return -1
        
        if self.head is None:
            return -1
        
        curr = self.head

        for i in range(index):
            curr = curr.next
        return curr.val

# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/
# Linked List Cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True
        return False


# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1214/
# Linked List Cycle II

# Return node where cycle starts
# First Approach, use a Hash Map: Time Complexity O(n), Space Complexity O(n)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        d = {}
        while head:
            if head in d:
                return head
            d[head] = head.val
            head = head.next
        return None


# Using Floyds Hare and Tortoise Algorithm with math
# 
def detectCycle(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    while head != slow:
        slow = slow.next
        head = head.next
    return head



# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/
# Intersection of Two Linked List

# My first solution using hash map: Time Complexity O(2n + m), where n is length of list A and m length of list B
# Space complexity O(n) since we create a Hashmap of A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # First Idea is to use a Hash Map 
        # Iterate each list one node at a time and check if there is a duplicate
        d = {}
        skipA, skipB = 0, 0
        if headA is None or headB is None:
            return None
        
        backupA = headA
        
        # Add all nodes from list A to dict
        while headA is not None:
                d[headA] = headA.val
                headA = headA.next
        # Check if any node of list B is the same as a node from listB 
        while headB is not None:
                if headB in d:
                    break
                headB = headB.next
                skipB += 1
        # If while runs through, there is no intersection
        else:
            return None
        # Walk through list A again to get skipA
        while backupA is not None:
            if backupA is headB:
                return backupA
            backupA = backupA.next
            skipA += 1
        return None

# -> Beats 84% in time, 23% in memory

# However 
# Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?
# Some Two pointer approach should yield better result

# Great visualization of algorithm in discussion
# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1215/discuss/49785/Java-solution-without-knowing-the-difference-in-len!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA and headB:
            A, B = headA, headB
            while A is not B:
                A = A.next if A else headB
                B = B.next if B else headA
            return A

# https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1296/
# Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# First go through logic with example
# Was really helpful for pointers here

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
        

