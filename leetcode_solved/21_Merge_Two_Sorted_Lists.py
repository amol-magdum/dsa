# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# time complexity: O(n + m) where n and m are lengths of list1 and list2
# space complexity: O(n + m) for the merged list

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists and compare node values
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach remaining nodes from either list
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        return dummy.next

# Test cases
print(mergeTwoLists([1,2,4], [1,3,4]))
print(mergeTwoLists([], []))  # []
print(mergeTwoLists([], [0])) # [0]
        
